# generator/project_templates.py
def get_clone_template(template_key: str, language: str) -> dict:
    if template_key == "pubg_clone":
        return {
            "game/README.md": "# PUBG Clone\n\nA simplified PUBG clone prototype.",
            "game/main.py": (
                "import pygame\n"
                "pygame.init()\n"
                "screen = pygame.display.set_mode((1280, 720))\n"
                "pygame.display.set_caption('PUBG Clone')\n"
                "running = True\n"
                "while running:\n"
                "    for event in pygame.event.get():\n"
                "        if event.type == pygame.QUIT:\n"
                "            running = False\n"
                "    screen.fill((34, 139, 34))\n"
                "    pygame.display.flip()\n"
                "pygame.quit()\n"
            ),
            "game/assets/map.txt": "Map data: [Complex map definition goes here]",
            "game/assets/characters.txt": "Character assets and definitions."
        }
    elif template_key == "nord_vpn_clone":
        return {
            "vpn/README.md": "# NordVPN Clone\n\nA simplified VPN clone prototype.",
            "vpn/app.py": (
                "from flask import Flask, jsonify\n"
                "app = Flask(__name__)\n\n"
                "@app.route('/connect')\n"
                "def connect():\n"
                "    return jsonify({'status': 'Connected to VPN clone'})\n\n"
                "if __name__ == '__main__':\n"
                "    app.run(debug=True)\n"
            ),
            "vpn/config.json": "{\n  \"servers\": [\"us1.example.com\", \"eu1.example.com\"]\n}"
        }
    elif template_key == "movie_website":
        return {
            "web/README.md": "# Custom Movie Website\n\nA website for movies.",
            "web/package.json": """{
  "name": "movie-website",
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
}""",
            "web/src/App.js": (
                "import React from 'react';\n\n"
                "function App() {\n"
                "  return (\n"
                "    <div>\n"
                "      <h1>Welcome to the Movie Website</h1>\n"
                "      <p>Enjoy our movie collection!</p>\n"
                "    </div>\n"
                "  );\n"
                "}\n\n"
                "export default App;\n"
            ),
            "web/public/index.html": (
                "<!DOCTYPE html>\n<html lang='en'>\n<head>\n"
                "  <meta charset='UTF-8'>\n"
                "  <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
                "  <title>Movie Website</title>\n"
                "</head>\n<body>\n"
                "  <div id='root'></div>\n"
                "</body>\n</html>\n"
            )
        }
    return {}
