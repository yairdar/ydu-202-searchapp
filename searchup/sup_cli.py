import typer

app = typer.Typer()


@app.command()
def info(as_cli=True):
    _msg_text = f"Welcome to searchup Control Center"
    if as_cli:
        typer.echo(_msg_text)
    return _msg_text

@app.command()
def start_server(name: str):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    app()
