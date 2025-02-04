# utils/file_manager.py
import os
import io
import zipfile

def create_directory_structure(files_dict: dict, base_path: str):
    for file_path, content in files_dict.items():
        full_path = os.path.join(base_path, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        mode = "wb" if isinstance(content, bytes) else "w"
        with open(full_path, mode) as f:
            f.write(content)

def zip_directory(directory_path: str) -> io.BytesIO:
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for root, _, files in os.walk(directory_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, start=directory_path)
                zip_file.write(full_path, arcname)
    zip_buffer.seek(0)
    return zip_buffer
