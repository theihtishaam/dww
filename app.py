# app.py
import os
import io
import uuid
import tempfile
from flask import Flask, render_template, request, jsonify, send_file, session, redirect, url_for
from flask_socketio import SocketIO, emit, join_room
from celery import Celery
from generator import (
    project_builder,
    chat_engine,
    feedback_processor,
    advanced_preview_engine
)
from utils.file_manager import create_directory_structure, zip_directory
from utils.logger import log_info
from database import db_session, init_db
from models import Project, ChatMessage

app = Flask(__name__)
app.config.from_object("config.Config")
socketio = SocketIO(app, message_queue=app.config.get("CELERY_BROKER_URL"), async_mode="threading")
celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
celery.conf.update(app.config)
init_db()

# In-memory storage for active projects (for demo purposes)
active_projects = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form.get("prompt", "")
    project_type = request.form.get("project_type", "multi")
    language = request.form.get("language", "python")
    # (Optional: Process file attachments via request.files if provided)
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    log_info(f"Generation request: prompt='{prompt}', type='{project_type}', language='{language}'")
    # Build the project file structure based on the prompt, with deep analysis and template selection.
    project_files = project_builder.build_project(prompt, project_type, language)
    
    # Asynchronously run error-checking, static analysis, and auto‑fixing (including security sanitization)
    task = error_check_and_fix.delay(project_files)
    fixed_files = task.get(timeout=120)
    
    project_id = str(uuid.uuid4())
    project = Project(
        id=project_id,
        prompt=prompt,
        project_type=project_type,
        language=language,
        files=str(fixed_files)
    )
    db_session.add(project)
    db_session.commit()
    
    active_projects[project_id] = fixed_files

    with tempfile.TemporaryDirectory() as tmpdirname:
        create_directory_structure(fixed_files, tmpdirname)
        zip_buffer = zip_directory(tmpdirname)
    
    session["project_id"] = project_id

    # Launch advanced live preview (which includes interactive selection and stubs for high‑graphic previews)
    advanced_preview_engine.launch_advanced_preview(project_id, fixed_files)

    response = send_file(zip_buffer, download_name="generated_project.zip", as_attachment=True)
    response.headers["X-Project-ID"] = project_id
    return response

@app.route("/chat")
def chat_page():
    project_id = session.get("project_id")
    if not project_id:
        return redirect(url_for("index"))
    messages = ChatMessage.query.filter_by(project_id=project_id).order_by(ChatMessage.timestamp).all()
    return render_template("chat.html", conversation=messages, project_id=project_id)

@app.route("/dashboard")
def dashboard():
    projects = Project.query.all()
    return render_template("dashboard.html", projects=projects)

@app.route("/preview/<project_id>")
def preview(project_id):
    preview_url = advanced_preview_engine.get_preview_url(project_id)
    return render_template("preview.html", preview_url=preview_url)

@app.route("/download/<project_id>")
def download(project_id):
    project = active_projects.get(project_id)
    if not project:
        return "Project not found.", 404
    with tempfile.TemporaryDirectory() as tmpdirname:
        create_directory_structure(project, tmpdirname)
        zip_buffer = zip_directory(tmpdirname)
    return send_file(zip_buffer, download_name="updated_project.zip", as_attachment=True)

# SocketIO events for real-time chat interaction
@socketio.on("join")
def on_join(data):
    project_id = data["project_id"]
    join_room(project_id)
    emit("status", {"msg": f"Joined room {project_id}"}, room=project_id)

@socketio.on("send_message")
def handle_message(data):
    project_id = data["project_id"]
    user_msg = data["message"]
    log_info(f"Chat message for project {project_id}: {user_msg}")
    chat_msg = ChatMessage(project_id=project_id, sender="user", message=user_msg)
    db_session.add(chat_msg)
    db_session.commit()
    task = process_chat_message.delay(project_id, user_msg)
    # The Celery task will process and emit the assistant's reply via SocketIO

@celery.task
def process_chat_message(project_id, user_msg):
    project_files = active_projects.get(project_id, {})
    response_text = chat_engine.generate_chat_response(user_msg, project_files)
    chat_msg = ChatMessage(project_id=project_id, sender="assistant", message=response_text)
    db_session.add(chat_msg)
    db_session.commit()
    updated_files = feedback_processor.process_update(user_msg, project_files)
    active_projects[project_id] = updated_files
    socketio.emit("receive_message", {"sender": "assistant", "message": response_text}, room=project_id)
    return response_text

@celery.task
def error_check_and_fix(project_files):
    from generator import error_checker
    fixed_files = error_checker.check_and_fix(project_files)
    return fixed_files

if __name__ == "__main__":
    socketio.run(app, debug=True)
