from kiro.prompts import (
    select_runtime,
    select_framework,
    ask_project_name,
    ask_language,
    select_database,
    select_orm
)

from kiro.state import KiroState
from kiro.generators import create_project
from kiro.database import setup_database
from kiro.installers import install_dependencies
from kiro.ui import show_success


def run_cli():
    print("\n⚡ Welcome to Kiro\n")

    state = KiroState()

    # Runtime
    state.runtime = select_runtime()
    print(f"\n✔ Selected runtime: {state.runtime}")

    # Language (Node.js only)
    if state.runtime == "Node.js":
        state.language = ask_language()
        print(f"\n✔ Language: {state.language}")

    # Framework
    state.framework = select_framework(state.runtime)
    print(f"\n✔ Selected framework: {state.framework}")

    # Project name
    state.project_name = ask_project_name()
    print(f"\n✔ Project name: {state.project_name}")

    # Database
    state.database = select_database()
    print(f"\n✔ Database: {state.database}")

    # ORM (only if a database was selected)
    state.orm = select_orm(
        state.runtime,
        state.database
    )

    if state.orm:
        print(f"\n✔ ORM: {state.orm}")

    # Generate project
    create_project(state)

    # Configure database
    setup_database(state)

    # Install dependencies
    install_dependencies(state)

    # Success message (always last)
    show_success(state)