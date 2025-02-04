# generator/chat_engine.py
from .code_generator import generate_code
from .prompt_analyzer import analyze_prompt

def generate_chat_response(user_message: str, project_files: dict) -> str:
    analysis = analyze_prompt(user_message)
    if "advanced_logic" in analysis.get("features", []):
        prompt = f"Explain improvements for the project based on: {user_message}"
    else:
        prompt = f"Respond conversationally to: {user_message}"
    response = generate_code(prompt, language="python")
    return response
