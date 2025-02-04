# generator/error_checker.py
def check_and_fix(files: dict) -> dict:
    fixed_files = {}
    for path, content in files.items():
        if isinstance(content, str) and "ERROR" in content:
            fixed_content = content.replace("ERROR", "# Auto-fixed error")
            fixed_files[path] = fixed_content
        else:
            fixed_files[path] = content
    return fixed_files
