from pathlib import Path

from searchup.blocks.djfedos_db.collections_manager import CollectionsManager


def test_list_collection(tmpdir):
    # arrange
    col = CollectionsManager(tmpdir)
    col.add_collection(name = "one")
    col.add_collection(name = "two")
    col.add_collection(name = "three")
    expected_collections = {Path(tmpdir, "one"), Path(tmpdir, "two"), Path(tmpdir, "three")}
    # act
    actual = set(col.list_collections())
    # assert
    assert expected_collections == actual


def test_add_collection(tmpdir):
    # arrange
    col = CollectionsManager(tmpdir)
    name = "tmp_dir_test"
    p = Path(tmpdir, name)
    # act
    col.add_collection(name)
    # assert
    assert p.exists()



def test_add_to_collection_web_api():
    # arrange
    from fastapi.testclient import TestClient
    from fapi_server import app
    client = TestClient(app)
    token1 = "tok_tester"

    # test for adding 1 dir
    # act
    response = client.get("/collections/add_item/" + token1)
    data = response.json()

    # assert
    assert response.status_code == 200
    assert data == token1

def test_get_collection_web_api():
    # arrange
    from fastapi.testclient import TestClient
    from fapi_server import app
    client = TestClient(app)
    token1 = "tok_tester"
    # act
    response = client.get("/collections/get_item/" + token1)
    data = response.json()
    # assert
    assert response.status_code == 200
    assert data["get collection. item_name_id"] == token1


#run test_add_to_collection_web_api before this test
def test_get_list_web_api():
    # arrange
    from fastapi.testclient import TestClient
    from fapi_server import app
    from fapi_server import col
    expected = []
    for i in col.wdir_p.iterdir():
        if i.is_dir():
            i = str(i)
            expected.append(i)
    client = TestClient(app)
    # act
    response = client.get("/collections/list")

    actual = response.json()
    # assert
    assert response.status_code == 200
    assert expected == actual
