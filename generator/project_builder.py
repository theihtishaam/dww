# generator/project_builder.py
from .code_generator import generate_code
from .image_generator import generate_icon
from .prompt_analyzer import analyze_prompt
from .project_templates import get_clone_template
from utils.security_manager import secure_code_files

def build_project(prompt: str, project_type: str, language: str) -> dict:
    files = {}
    analysis = analyze_prompt(prompt)
    clone_template_key = analysis.get("clone_template")
    
    if clone_template_key:
        files.update(get_clone_template(clone_template_key, language))
    else:
        files["README.md"] = (
            f"# Generated Project\n\n"
            f"Prompt: {prompt}\n"
            f"Project Type: {project_type}\n"
            f"Language: {language}\n"
            f"Analysis: {analysis}\n\n"
            f"Generated by Ultra Advanced AI Assistant."
        )
        if project_type.lower() == "mobile":
            files["mobile/README.md"] = "# Mobile App\n\nA generated React Native mobile app."
            files["mobile/package.json"] = """{
  "name": "mobile-app",
  "version": "1.0.0",
  "main": "App.js",
  "scripts": {
    "start": "react-native start",
    "android": "react-native run-android",
    "ios": "react-native run-ios"
  },
  "dependencies": {
    "react": "17.0.1",
    "react-native": "0.64.0"
  }
}"""
            files["mobile/App.js"] = """import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const App = () => (
  <View style={styles.container}>
    <Text>Welcome to your Mobile App!</Text>
  </View>
);

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
"""
        elif project_type.lower() == "web":
            files["web/README.md"] = "# Web App\n\nA generated React web application."
            files["web/package.json"] = """{
  "name": "web-app",
  "version": "1.0.0",
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build"
  },
  "dependencies": {
    "react": "^17.0.1",
    "react-dom": "^17.0.1",
    "react-scripts": "4.0.3"
  }
}"""
            files["web/src/App.js"] = """import React from 'react';

function App() {
  return (
    <div>
      <h1>Welcome to your Web App!</h1>
    </div>
  );
}

export default App;
"""
            files["web/public/index.html"] = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Web App</title>
</head>
<body>
  <div id="root"></div>
</body>
</html>
"""
        elif project_type.lower() == "python":
            files["python/README.md"] = "# Python App\n\nA generated Flask application."
            files["python/app.py"] = """from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to your Flask App!"

if __name__ == '__main__':
    app.run(debug=True)
"""
            files["python/requirements.txt"] = "Flask==2.0.1"
        elif project_type.lower() == "game":
            files["game/README.md"] = "# Game App\n\nA generated game application."
            files["game/main.py"] = """import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Generated Game')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((200, 200, 200))
    pygame.display.flip()
pygame.quit()
"""
            files["game/requirements.txt"] = "pygame"
        else:
            files["custom/README.md"] = "# Multi-Language App\n\nA project with multiple languages."
            py_code = generate_code(f"Create a Python function for: {prompt}", "python")
            files["custom/greet.py"] = py_code
            js_code = generate_code(f"Create a JavaScript function for: {prompt}", "javascript")
            files["custom/greet.js"] = js_code

    try:
        icon_data = generate_icon(prompt)
        files["assets/icon.png"] = icon_data
    except Exception as e:
        files["assets/icon.png"] = f"Error generating icon: {e}"

    secured_files = secure_code_files(files)
    return secured_files
