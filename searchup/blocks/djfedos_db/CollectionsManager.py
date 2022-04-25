import pathlib
from pathlib import Path


class CollectionsManager:

    def __init__(self, path_to_wdir):
        self.wdir_p = Path(path_to_wdir)
        self.wdir_p.mkdir(exist_ok=True, parents=True)

    def add_collection(self, name, kind='tokens_trie'):
        Path(name).mkdir(exist_ok=True, parents=True)
        p = Path(name) # correct path
        (p / f"{kind}.txt").write_text("")
        print(pathlib.Path.is_dir())
        print(pathlib.Path.is_file())


        #create new folder if nor exist

    def get_collection(self, name):
        #return name

    def list_collections(self):
        res = list(self.wdir_p.iterdir())
        return res