# generator/static_analyzer.py
import subprocess

def run_flake8(file_path: str) -> str:
    try:
        result = subprocess.run(["flake8", file_path], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

def auto_fix_with_autopep8(file_path: str) -> None:
    try:
        subprocess.run(["autopep8", "--in-place", file_path], check=True)
    except Exception:
        pass

def analyze_and_fix(file_path: str) -> None:
    issues = run_flake8(file_path)
    if issues:
        auto_fix_with_autopep8(file_path)
