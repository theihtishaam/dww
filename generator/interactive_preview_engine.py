# generator/interactive_preview_engine.py
from flask import request

def process_interactive_selection(selection_data: dict, project_files: dict) -> dict:
    # Stub: Process selection data to update only the selected component
    if "update_part" in selection_data:
        part = selection_data["update_part"]
        if part == "header":
            project_files["web/src/Header.js"] = "// Updated Header component code based on selection"
    return project_files

def get_interactive_update_payload():
    return request.get_json()
