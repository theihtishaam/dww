# generator/advanced_preview_engine.py
import os
import tempfile
from utils.file_manager import create_directory_structure

_preview_registry = {}
_unreal_registry = {}
_graphics_registry = {}

def launch_advanced_preview(project_id: str, files: dict):
    # Standard web/mobile preview
    preview_path = os.path.join(tempfile.gettempdir(), f"advanced_preview_{project_id}")
    os.makedirs(preview_path, exist_ok=True)
    create_directory_structure(files, preview_path)
    _preview_registry[project_id] = f"/static/preview/{project_id}/index.html"

def get_preview_url(project_id: str) -> str:
    # Prefer Unreal or high‑graphics preview if available
    if project_id in _unreal_registry:
        return _unreal_registry[project_id]
    if project_id in _graphics_registry:
        return _graphics_registry[project_id]
    return _preview_registry.get(project_id, "#")

def launch_unreal_preview(project_id: str, files: dict):
    preview_path = os.path.join(tempfile.gettempdir(), f"unreal_preview_{project_id}")
    os.makedirs(preview_path, exist_ok=True)
    create_directory_structure(files, preview_path)
    _unreal_registry[project_id] = f"/static/unreal_previews/{project_id}/index.html"

def launch_graphics_preview(project_id: str, files: dict):
    preview_path = os.path.join(tempfile.gettempdir(), f"graphics_preview_{project_id}")
    os.makedirs(preview_path, exist_ok=True)
    create_directory_structure(files, preview_path)
    _graphics_registry[project_id] = f"/static/graphics_previews/{project_id}/index.html"
