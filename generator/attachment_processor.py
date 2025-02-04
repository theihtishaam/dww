# generator/attachment_processor.py
import zipfile
import os
import tempfile
import json

def process_uploaded_zip(zip_file_bytes: bytes) -> dict:
    temp_zip = tempfile.NamedTemporaryFile(delete=False, suffix=".zip")
    temp_zip.write(zip_file_bytes)
    temp_zip.close()
    extract_path = tempfile.mkdtemp()
    with zipfile.ZipFile(temp_zip.name, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    result = {}
    for root, dirs, files in os.walk(extract_path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    result[os.path.join(root, file)] = f.read()
            except Exception:
                pass
    os.remove(temp_zip.name)
    return result

def process_figma_file(figma_file_bytes: bytes) -> dict:
    try:
        data = json.loads(figma_file_bytes.decode("utf-8"))
        return {"figma_data": data}
    except Exception as e:
        return {"error": str(e)}
