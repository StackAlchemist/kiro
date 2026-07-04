import typer
app = typer.Typer()

@app.command() #decorator for commands
def create():
    print("Welcome to Kiro 🚀")