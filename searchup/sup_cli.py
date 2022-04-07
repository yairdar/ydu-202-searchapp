import typer

app = typer.Typer()


@app.command()
def info(name: str):
    typer.echo(f"Hello {name}")

@app.command()
def start_server(name: str):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    app()
