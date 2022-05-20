from fastapi import FastAPI
from pathlib import Path
app = FastAPI()

class CollectionsManager:

    def __init__(self, path_to_wdir = None):
        if path_to_wdir == None:
            path_to_wdir = Path.cwd()
        self.wdir_p = Path(path_to_wdir)
        self.wdir_p = Path(path_to_wdir)
        self.wdir_p.mkdir(exist_ok=True, parents=True)


    def add_collection(self, name, kind='tokens_trie'):
        Path(self.wdir_p, name).mkdir(exist_ok=True, parents=True)
        p = Path(name)
        return p.name

    def get_collection(self, name):
        p = Path("__wdir", name)
        if p.exists():
            return p.name
        else:
            return None

    def list_collections(self):  # remove absolut path and chang to __wdir sub folders
        res = []
        print(self.wdir_p)
        for i in self.wdir_p.iterdir():
            if i.is_dir():
                res.append(i)
        print(res)
        return res


# def test_list_collection(tmpdir):
#     # arrange
#     col = CollectionsManager(tmpdir)
#     col.add_collection(name = "one")
#     col.add_collection(name = "two")
#     col.add_collection(name = "three")
#     expected_collections = {Path(tmpdir, "one"), Path(tmpdir, "two"), Path(tmpdir, "three")}
#     # act
#     actual = set(col.list_collections())
#     # assert
#     assert expected_collections == actual


# def test_add_collection(tmpdir):
#     # arrange
#     col = CollectionsManager(tmpdir)
#     name = "tmp_dir_test"
#     p = Path(tmpdir, name)
#     # act
#     col.add_collection(name)
#     # assert
#     assert p.exists()


# def test_add_to_collection_web_api():
#     # arrange
#     from fastapi import FastAPI
#     from fastapi.testclient import TestClient
#     from fapi_server import app
#     client = TestClient(app)
#     token1 = "tok_tester"
#
#     # test for adding 1 dir
#     # act
#     response = client.get("/collections/add_item/" + token1)
#     data = response.json()
#
#     # assert
#     assert response.status_code == 200
#     assert data == token1

# def test_get_collection_web_api():
#     # arrange
#     from fastapi.testclient import TestClient
#     from fapi_server import app
#     client = TestClient(app)
#     token1 = "tok_tester"
#     # act
#     response = client.get("/collections/get_item/" + token1)
#     data = response.json()
#     # assert
#     assert response.status_code == 200
#     assert data["get collection. item_name_id"] == token1


#run test_add_to_collection_web_api before this test
def test_get_list_web_api():
    # arrange
    from fastapi.testclient import TestClient
    from fapi_server import app
    expected = Path.cwd()
    client = TestClient(app)
    # act
    response = client.get("/collections/list")

    actual = response.json()
    # assert
    assert response.status_code == 200
    assert expected in actual


if __name__ == '__main__':
    name = "__wdir"

    col = CollectionsManager(name)
    col.list_collections()
    #print(col.add_collection(name))