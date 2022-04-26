import pathlib

from searchup.blocks.djfedos_db.fapi_server import app


def test_add_collection():
    from fastapi import FastAPI
    from fastapi.testclient import TestClient

    #client = TestClient(app)

    # act

    #response = client.get("/load_db/2466_tokens.txt")
    #data = response.json()
    #print(pathlib.Path.is_dir())
    #print(pathlib.Path.is_file())
    # assert
    assert pathlib.Path.is_dir()
    pathlib.Path.is_file()


def test_benchmark_load_db(tmpdir):
    tfk = TokensFileCreator(tmpdir)
    bench_file = tfk.create_token_file(num_lines, max_length)