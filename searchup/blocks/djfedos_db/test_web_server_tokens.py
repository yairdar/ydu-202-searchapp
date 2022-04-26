

def test_read_root():
    # arrange
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    from fapi_server import app
    client = TestClient(app)

    # act
    response = client.get("/")
    data = response.json()

    # assert
    assert response.status_code == 200
    assert data["msg"] == {"Hello": "World"}


def test_load_db():
    # arrange
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    from fapi_server import app
    client = TestClient(app)

    # act
    response = client.get("/load_db/2466_tokens.txt")
    data = response.json()

    # assert
    assert response.status_code == 200
    assert data["len"] == 26


def test_dump_db():
    # arrange
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    from fapi_server import app
    client = TestClient(app)
    # see load_db method tweak to take any file path if needed
    client.get("/load_db/tests?q=tokens.txt")
    expected_dump_content = {'marsaba', 'maramba', 'man', 'may', 'bar', 'baron', 'banya', 'raba', 'rab'}

    # act
    response = client.get('/dump_db/api_test_db_dump')
    data = response.json()
    actual_dump_content = set()
    with open('api_test_db_dump/token_db.txt', 'r') as dump_file:
        for line in dump_file:
            line = line.strip()
            actual_dump_content.add(line)

    # assert
    assert response.status_code == 200
    assert data["path"] == 'api_test_db_dump'
    assert actual_dump_content == expected_dump_content


def test_add_to_db():
    # arrange
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    from fapi_server import app
    client = TestClient(app)
    token1 = "tok_tester"
    token2 = "tok_tester_2"
    token3 = "game_changer"

    # test for adding 1 token
    # act
    response = client.get("/add_to_db/" + token1)
    data = response.json()
 
    # assert
    assert response.status_code == 200
    assert data["token"] == token1
    assert data["len"] >= 1

    response = client.get("/get_suggestions/" + token1)
    data = response.json()
    assert token1 in data["result"]
    

def test_get_suggestions():
    # arrange
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    from fapi_server import app
    client = TestClient(app)
    client.get("/load_db/2466_tokens.txt")
    prefix = "sympt"
    
    # act
    response = client.get("/get_suggestions/" + prefix)
    data = response.json()

    # assert
    assert response.status_code == 200
    assert data["prefix"] == prefix
    assert data["limit"] == 10
    assert data["result"] == ['symptomatic']

# add get