# generator/code_generator.py
import re
from transformers import pipeline

generator_pipeline = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

def generate_code(prompt: str, language: str = "python") -> str:
    if language.lower() == "python":
        prompt = f"# Python code generation\n{prompt}\n"
    elif language.lower() in ["javascript", "js"]:
        prompt = f"// JavaScript code generation\n{prompt}\n"
    elif language.lower() == "java":
        prompt = f"// Java code generation\n{prompt}\n"
    else:
        prompt = f"{prompt}\n"
    outputs = generator_pipeline(prompt, max_length=1024, do_sample=True, temperature=0.7)
    generated_text = outputs[0]['generated_text']
    cleaned_text = re.sub(re.escape(prompt), "", generated_text, count=1).strip()
    return cleaned_text
