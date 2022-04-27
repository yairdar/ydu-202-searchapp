import typer

app = typer.Typer()


@app.command()
def info(as_cli=True):
    _msg_text = f"Welcome to searchup Control Center"
    if as_cli:
        typer.echo(_msg_text)
    return _msg_text

@app.command()
def start_server(name: str = 'djfedos_db'):
    supported = "djfedos_db".split()
    if name == 'djfedos_db':
        import sys
        from pathlib import Path
        me_par_p = Path(__file__).parent
        targ_lib_p = me_par_p / 'block' / 'djfedos_db'
        sys.path.insert(0, str(me_par_p.absolute()))
        sys.path.insert(0, str(targ_lib_p.absolute()))
        print(str(targ_lib_p.absolute()))
        from searchup.blocks.djfedos_db import fapi_server
        fapi_server.main()
    else:
        raise ValueError(f"wrong name = {name}. should be on of {supported}")
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    app()
