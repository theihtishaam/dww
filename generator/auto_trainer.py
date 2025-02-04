# generator/auto_trainer.py
import uuid
from models import Feedback
from database import db_session

def log_feedback(project_id: str, message: str, rating: str):
    feedback = Feedback(id=str(uuid.uuid4()), project_id=project_id, message=message, rating=rating)
    db_session.add(feedback)
    db_session.commit()
    # Stub: Trigger model retraining if feedback threshold is met.
    return "Feedback logged."
