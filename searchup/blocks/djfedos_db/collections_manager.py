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


if __name__ == '__main__':
    name = "__wdir"

    col = CollectionsManager(name)
    col.list_collections()
    #print(col.add_collection(name))