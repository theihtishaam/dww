# utils/resource_manager.py
import psutil

def get_cpu_usage() -> float:
    return psutil.cpu_percent(interval=1)

def get_memory_usage() -> float:
    mem = psutil.virtual_memory()
    return mem.percent
