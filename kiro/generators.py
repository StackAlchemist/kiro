# Creates files/folders
import os
from pathlib import Path

def create_project(state):
    base_path = Path(state.project_name)
    base_path.mkdir(exist_ok=True)

    # create project folder

    (base_path / "src").mkdir(exist_ok=True)
    (base_path / "src" / "routes").mkdir(parents=True, exist_ok=True)

    if state.runtime == "Node.js":
        main_file = base_path / "src" / "index.js"
        main_file.write_text(
             """console.log("Kiro project running 🚀")"""
        )

    elif state.runtime == "Python":
        main_file = base_path / "src" / "main.py"
        main_file.write_text(
            """print("Kiro project running 🚀")"""
        )

    elif state.runtime == "Go":
        main_file = base_path / "src" / "main.go"
        main_file.write_text(
            """package main
            func main() {
                fmt.Println("Kiro project running 🚀")
            }"""
        )
        
    print(f"\n📁 Created project: {project_name}")