# generator/advanced_graphics_preview.py
import os
import tempfile
from utils.file_manager import create_directory_structure

_graphics_preview_registry = {}

def launch_advanced_graphics_preview(project_id: str, files: dict):
    preview_path = os.path.join(tempfile.gettempdir(), f"advanced_graphics_preview_{project_id}")
    os.makedirs(preview_path, exist_ok=True)
    create_directory_structure(files, preview_path)
    _graphics_preview_registry[project_id] = f"/static/advanced_graphics_previews/{project_id}/index.html"

def get_advanced_graphics_preview_url(project_id: str) -> str:
    return _graphics_preview_registry.get(project_id, "#")
