# generator/feedback_processor.py
from .code_generator import generate_code

def process_update(update_prompt: str, project_files: dict) -> dict:
    if "README.md" in project_files:
        original = project_files["README.md"]
        addition = f"\n\n## Update:\n{update_prompt}\n"
        project_files["README.md"] = original + addition
    else:
        project_files["README.md"] = f"# Updated README\n{update_prompt}\n"
    if "python" in update_prompt.lower():
        new_code = generate_code(f"Update Python code based on: {update_prompt}", "python")
        project_files["update/updated_code.py"] = new_code
    if "javascript" in update_prompt.lower():
        new_code = generate_code(f"Update JavaScript code based on: {update_prompt}", "javascript")
        project_files["update/updated_code.js"] = new_code
    return project_files
