import pathlib
from pathlib import Path


class CollectionsManager:

    def __init__(self, path_to_wdir):
        self.wdir_p = Path(path_to_wdir)
        self.wdir_p.mkdir(exist_ok=True, parents=True)

    def add_collection(self, name, kind='tokens_trie'):# create new folder if nor exist
        Path(Path.cwd(),"__wdir",name).mkdir(exist_ok=True, parents=True)
        p = Path(name)  # correct path

        #(p / f"{kind}.txt").write_text("")


    def get_collection(self, name):
        p = Path("__wdir",name)
        #print(p)
        if p.exists():
            print("Exists", p.exists(),p)
            return p
        else:
            print("Exists", p.exists())
            return p

    def list_collections(self):
        res = list(self.wdir_p.iterdir())
        return res


# def test_list_collection():
#     # arrange
#     col = CollectionsManager("name")
#     expected_collections = []
#     # act
#     actual = col.list_collections()
#     # assert
#     assert expected_collections == actual


# def test_add_collection():
#     # arrange
#     col = CollectionsManager("__some2")
#
#     # act
#
#     col.add_collection(name="asd")
#     # assert
#     assert expected_collections == actual

if __name__ == '__main__':
    name = "__wdir"
    col = CollectionsManager(name)
    #col.add_collection("new_name")
    col.get_collection("name")
    #col.get_collection("__some")
    #col.list_collections()