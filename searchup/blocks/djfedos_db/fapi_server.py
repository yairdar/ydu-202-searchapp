from pathlib import Path
from typing import Optional
import uvicorn
from fastapi import FastAPI
import lib_search_sdk

app = FastAPI()


class DjfedosDbFacade:
    """Adapter Class to underliyng actual implementation 
    currently we hardcoded djfedeos implementation from https://github.com/djfedos/djfedos-search
    """
    
    def __init__(self) -> None:

        self.lib_search_sdk = lib_search_sdk    #what is it
        self._db: dict = self.lib_search_sdk.init_db()
        
    def add_to_db(self, token):
        self.lib_search_sdk.add_to_db(self._db, token)
        return self
        
    def load_db(self, path: str):#read file
        self._db = self.lib_search_sdk.load_db(path=path)
        return self
    
    def get_suggestions(self, prefix, limit=10):
        res = self.lib_search_sdk.get_suggestions(self._db, prefix=prefix, limit=limit)
        return res
    
_impl_db = DjfedosDbFacade()

@app.get("/")
def read_root():
    res = {
        "msg": {"Hello": "World"},
        "menu": {
            "recreate": [
              "/load_db/2466_tokens.txt",
            ],
            "update": [
              "/add_to_db/token1",
              "/add_to_db/token2",
            ],
            "query":[
              "/get_suggestions/token",
            ]
        }
    }

    return res


@app.get("/load_db/{path}")
def load_db(path: str, q: Optional[str] = None):
    print("Get load_db from fapi server", path)
    _impl_db.load_db(path=path)
    resp = {"path": path, "len": len(_impl_db._db)}

    return resp

@app.get("/add_to_db/{token}")
def add_to_db(token: str, q: Optional[str] = None):
    print("add_to_db",token)
    _impl_db.add_to_db(token=token)
    resp =  {"token": token, "len": len(_impl_db._db)}
    return resp

@app.get("/get_suggestions/{prefix}")
def read_item(prefix: str, limit: Optional[int] = 10):
    res = _impl_db.get_suggestions(prefix=prefix, limit=limit)
    resp = {"prefix": prefix, "limit": limit, "result": res}
    return resp

@app.get("/get_suggestions/{prefix}")
def read_item(prefix: str, limit: Optional[int] = 10):
    res = _impl_db.get_suggestions(prefix=prefix, limit=limit)
    resp = {"prefix": prefix, "limit": limit, "result": res}
    return resp
# create def for fined movies

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


def main():
    uvicorn.run(app, host="0.0.0.0", port=18000)

# create a new director
def add_new_dir():
    filepath = Path("temp/test.txt")
    filepath.parent.mkdir(parents=True, exist_ok=True)


def get_dir(): #get a home dir
    home = Path.home()
    return home


def create_file():  #or create a new file each time?
    myfile = Path(Path.home(), "file.txt")
    myfile.touch(exist_ok=True)
    f = open(myfile)


def get_list_dir():# get a Listing subdirectories:
    p = Path('.')
    return [x for x in p.iterdir() if x.is_dir()]


if __name__ == "__main__":
    main()
