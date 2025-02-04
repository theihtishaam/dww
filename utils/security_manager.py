# utils/security_manager.py
import re

def perform_security_checks(code: str) -> bool:
    dangerous_patterns = [
        r"os\.system", r"eval\(", r"exec\(", r"subprocess\.Popen",
        r"__import__", r"input\(", r"open\("
    ]
    for pattern in dangerous_patterns:
        if re.search(pattern, code):
            return False
    return True

def secure_code_files(files: dict) -> dict:
    secured_files = {}
    for path, content in files.items():
        if isinstance(content, str):
            for pattern in [r"os\.system", r"eval\(", r"exec\("]:
                content = re.sub(pattern, f"# Removed dangerous call: {pattern}", content)
            content = content.replace("<script>", "&lt;script&gt;").replace("</script>", "&lt;/script&gt;")
        secured_files[path] = content
    return secured_files
