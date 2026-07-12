from pathlib import Path


def setup_database(state):
    if state.database == "None":
        return

    project = Path(state.project_name)
    env = project / ".env"

    if not env.exists():
        env.write_text("")

    if state.database == "PostgreSQL":
        env.write_text(
        "DATABASE_URL=postgresql://username:password@localhost:5432/mydb\n"
        )
    elif state.database == "MySQL":
        env.write_text(
        "DATABASE_URL=mysql://root:password@localhost:3306/mydb\n"
        )
    elif state.database == "SQLite":
        env.write_text(
        "DATABASE_URL=file:./database.db\n"
        )
    elif state.database == "MongoDB":
        env.write_text(
        "DATABASE_URL=mongodb://localhost:27017/mydb\n"
        )


    print(f"🗄 Setting up {state.database}...")