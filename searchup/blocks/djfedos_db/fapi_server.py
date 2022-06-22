from pathlib import Path
from typing import Optional
import uvicorn
from fastapi import FastAPI
import lib_search_sdk
from collections_manager import CollectionsManager
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

    def dump_db(self, path: str):
        self.lib_search_sdk.dump_db(self._db, path)
        return self
    
    def get_suggestions(self, prefix, limit=10):
        res = self.lib_search_sdk.get_suggestions(self._db, prefix=prefix, limit=limit)
        return res
    
_impl_db = DjfedosDbFacade()
col = CollectionsManager("web_api_wdir")
#col = CollectionsManager()

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
    # here is a workaround to load db from folders
    if q:
        path += '/' + q
    # so load them like this: /load_db/%folder_name%?q=%rest_of_the_path%
    _impl_db.load_db(path=path)
    resp = {"path": path, "len": len(_impl_db._db)}

    return resp

@app.get("/dump_db/{path}")
def dump_db(path: str):
    _impl_db.dump_db(path)
    resp = {"path": path}
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


# end points to work with collection
# --- collections API ---


@app.post("/collections/set_item/{item_name_id}")
def set_collection_item(item_name_id):
    """
    to add a new collection to collections we go here
    to initialize an empty collection as well
    """
    print(f"set collection: item_name_id: {item_name_id}")
    return {"set collection: item_name_id": item_name_id}


@app.get("/collections/get_item/{item_name_id}")
def get_collection_item(item_name_id):
    """
    to get the list of our collections we go here
    """
    print(f"get collection. item_name_id: {item_name_id}")
    return {"get collection. item_name_id": item_name_id}


@app.get("/collections/search/{prefix}")
def search_in_all_collections(prefix):
    """
    to search through all collections we go here
    """
    print(f"we search in ALL collections now. prefix: {prefix}")
    return {"we search in ALL collections now. prefix": prefix}


# --- items API ---


@app.post("/collection/{item_name_id}/set_item/{item_token}")
def set_item(item_name_id, item_token):
    """
    to add an item to collection we go here
    """
    print(f"we set item to collection {item_name_id}. item_token: {item_token}")
    return {"we set item to collection. item_token": item_token}


@app.get("/collection/{item_name_id}/get_item/{item_token}")
def get_item(item_name_id, item_token):
    """
    to get an item from collection we go here
    """
    print(f"we get item from collection {item_name_id}. item_token: {item_token}")
    return {"we get item from collection. item_token": item_token}


@app.get("/collection/{item_name_id}/get_suggestions/{prefix}")
def search_in_one_collection(item_name_id, prefix, limit: Optional[int] = 10):
    """
    to search through collection we go here
    it corresponds to get_suggestions method that we had before
    (calling function, not restful, but we'll call it...)
    """
    print(f"we search in ONE collection {item_name_id} with limit {limit} now. prefix: {prefix}")
    return {"we search in ONE collection now. prefix": prefix}

  
@app.get("/collections/add_item/{item_name_id}")
def add_collection_item(item_name_id):
    col.add_collection(item_name_id)
    return(item_name_id)

  
@app.get("/collections/get_item/{item_name_id}")
def get_collection_item(item_name_id):
    return (col.get_collection(item_name_id))

  
@app.get("/collections/list")
def list_collections():
    return (col.list_collections())

  
def main():
    uvicorn.run(app, host="0.0.0.0", port=18000)

    
# create a new directory
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
