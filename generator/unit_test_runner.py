# generator/unit_test_runner.py
import subprocess

def run_unit_tests(test_directory: str) -> str:
    try:
        result = subprocess.run(["pytest", test_directory], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)
