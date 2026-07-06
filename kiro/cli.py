from kiro.prompts import (
    select_runtime,
    select_framework,
    ask_project_name,
    ask_language,
    confirm_install_dependencies,
    confirm_git_init
)

from kiro.state import KiroState
from kiro.generators import create_project
from kiro.installers import install_dependencies


def run_cli():
    print("\n⚡ Welcome to Kiro\n")

    state = KiroState()

    state.runtime = select_runtime()
    print(f"\n✔ Selected runtime: {state.runtime}")

    # Only ask language for Node.js
    if state.runtime == "Node.js":
        state.language = ask_language()
        print(f"\n✔ Language: {state.language}")

    state.framework = select_framework(state.runtime)
    print(f"\n✔ Selected framework: {state.framework}")

    state.project_name = ask_project_name()
    print(f"\n✔ Project name: {state.project_name}")

    create_project(state)

    if confirm_install_dependencies():
        install_dependencies(state)