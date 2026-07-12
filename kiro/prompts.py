# Questionary prompts
import questionary
import typer

def confirm_install_dependencies():
    return typer.confirm(
        "Install dependencies?",
        default=True
    )


def confirm_git_init():
    return typer.confirm(
        "Initialize Git repository?",
        default=True
    )

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
    return questionary.text(
        "project name?",
        validate=lambda text: len(text.strip()) > 0 or "Project name cannot be empty"
        ).ask()

def ask_language():
    return questionary.select(
        "Choose language",
        choices=[
            "JavaScript",
            "TypeScript"
        ]
    ).ask()

    return choice

def select_database():
    return questionary.select(
        "Select database",
        choices=[
            "PostgreSQL",
            "MySQL",
            "SQLite",
            "MongoDB",
            "None",
        ]
    ).ask()
    return choice

import questionary

def select_orm(runtime, database):
    choices = []

    if runtime == "Node.js":
        if database == "MongoDB":
            choices = [
                "Mongoose",
                "None"
            ]
        elif database != "None":
            choices = [
                "Prisma",
                "Drizzle",
                "TypeORM",
                "None"
            ]
        else:
            return None

    elif runtime == "Python":
        if database == "MongoDB":
            choices = [
                "MongoEngine",
                "Beanie",
                "None"
            ]
        elif database != "None":
            choices = [
                "SQLAlchemy",
                "Tortoise ORM",
                "None"
            ]
        else:
            return None

    elif runtime == "Go":
        if database != "None":
            choices = [
                "GORM",
                "sqlx",
                "None"
            ]
        else:
            return None

    return questionary.select(
        "Choose ORM",
        choices=choices
    ).ask()