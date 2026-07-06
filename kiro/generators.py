# Creates files/folders
import os
from pathlib import Path
import shutil
from kiro.utils.files import replace_placeholders
from kiro.ui import show_success
from kiro.installers import install_dependencies



def create_project(state):
    base_path = Path(state.project_name)
    base_path.mkdir(exist_ok=True)

    template_path = get_template_path(state)

    if template_path and template_path.exists():
        shutil.copytree(
            template_path,
            base_path,
            dirs_exist_ok=True
        )

        replace_placeholders(base_path, state)

    show_success(state)



def get_template_path(state):
    base = Path("kiro") / "templates"

    if state.runtime == "Node.js":
        framework = state.framework.lower()

        language = state.language.lower()  # javascript / typescript

        return base / "node" / framework / language

    if state.runtime == "Python":
        framework = state.framework.lower()
        return base / "python" / framework

    if state.runtime == "Go":
        framework = state.framework.lower()
        return base / "go" / framework

    return None