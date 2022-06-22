
from pathlib import Path


class CollectionsManager:

    def __init__(self, path_to_wdir = None):
        if path_to_wdir == None:
            path_to_wdir = Path.cwd()
        self.wdir_p = Path(path_to_wdir)
        self.wdir_p.mkdir(exist_ok=True, parents=True)

    def add_collection(self, name, kind='tokens_trie'):
        Path(self.wdir_p, name).mkdir(exist_ok=True, parents=True)
        p = Path(name)
        return p.name


    def get_collection(self, name):
        p = Path("__wdir", name)
        #print(p)
        if p.exists():
            print("Exists", p)
            return p.name
        else:
            print("Doesn't exist")
            return None

    def list_collections(self):
        res = []
        for i in self.wdir_p.iterdir():
            if i.is_dir():
                res.append(i)
        return res


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

# @app.post("/collections/set_item/{item_name_id}")
# def set_collection_item(item_name_id):
#   ...
#
# @app.get("/collections/get_item/{item_name_id}")
# def get_collection_item(item_name_id):
#    ...
#
# @app.get("/collections/list")
# def list_collections(prefix):


if __name__ == '__main__':
    name = "__wdir"
    col = CollectionsManager(name)