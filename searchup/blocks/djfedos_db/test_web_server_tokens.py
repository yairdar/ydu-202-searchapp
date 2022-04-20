
# from pathlib import Path
# import sys
# _me_parent = Path(__file__).absolute().parent.parent
# sys.path.append(_me_parent)



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
    # print("\n client: path is " + data["path"])
    # print("\n client: len is " + str(data["len"]))

    # assert
    assert response.status_code == 200
    # assert data["path"] == "data/tokens1.txt"
    assert data["len"] == 26


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


    # # test for adding 2nd token that start with same char
    # # act
    # response = client.get("/add_to_db/" + token2)
    # data = response.json()
  
    # # assert
    # assert response.status_code == 200
    # assert data["token"] == token2
    # assert data["len"] == 1

    # # test for adding 3rd token that start with different char
    # # act
    # response = client.get("/add_to_db/" + token3)
    # data = response.json()
  
    # # assert
    # assert response.status_code == 200
    # assert data["token"] == token3
    # assert data["len"] == 2


    

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

