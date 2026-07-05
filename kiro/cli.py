from kiro.prompts import select_runtime, select_framework, ask_project_name
from kiro.state import KiroState
from kiro.generators import create_project

def run_cli():
    print("\n⚡ Welcome to Kiro\n")

    state = KiroState()

    state.runtime = select_runtime()
    print(f"\n✔ Selected runtime: {state.runtime}")

    state.framework = select_framework(state.runtime)
    print(f"\n✔ Selected framework: {state.framework}")

    state.project_name = ask_project_name()
    print(f"\n✔ Project name: {state.project_name}")

    create_project(state)