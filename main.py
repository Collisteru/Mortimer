from typing import Optional

import typer

app = typer.Typer()

@app.command
def init(location: str):
    print(f"Initializing booklist at {location}")
    

def hello(name: Optional[str] = None):
    if name:
        typer.echo(f"Hello {name}")
    else:
        typer.echo("Hello World!")

@app.command()
def bye(name: Optional[str] = None):
    if name:
        type.echo(f"Bye {name}")
    else:
        typer.echo("Goodbye!")


if __name__ == "__main__":
    app()
