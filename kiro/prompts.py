# Questionary prompts
import questionary

def select_runtime():
    return questionary.select(
        "Which runtime do you want to use?",
        choices=[
            "Node.js",
            "Python",
            "Go"
        ]
    ).ask()


def select_framework(runtime: str):
    if runtime == "Node.js":
        choices = ["Express", "Fastify", "NestJS"]
    elif runtime == "Python":
        choices = ["FastAPI", "Flask", "Django"]
    else:
        choices = ["None"]

    return questionary.select(
        "Choose a framework",
        choices=choices,
    ).ask()

def ask_project_name():
    return questionary.text("project name?").ask()