from typing import Optional
import uvicorn
from fastapi import FastAPI
from searchup.blocks.djfedos_db import lib_search_sdk

app = FastAPI()


class DjfedosDbFacade:
    """Adapter Class to underliyng actual implementation 
    currently we hardcoded djfedeos implementation from https://github.com/djfedos/djfedos-search
    """
    
    def __init__(self) -> None:
        
        self.lib_search_sdk = lib_search_sdk
        self._db: dict = self.lib_search_sdk.init_db()
        
    def add_to_db(self, token):
        self.lib_search_sdk.add_to_db(self._db, token)
        return self
        
    def load_db(self, path: str):
        self._db = self.lib_search_sdk.load_db(path=path)
        return self
    
    def get_suggestions(self, prefix, limit=10):
        res = self.lib_search_sdk.get_suggestions(self._db, prefix=prefix, limit=limit)
        return res
    
_impl_db = DjfedosDbFacade()

@app.get("/")
def read_root():
    res =  {
        "msg": {"Hello": "World"},
        "menu": {
            "recreate": [
              "/load_db/searchup/blocks/djfedos_db/2466_tokens.txt",
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
    _impl_db.load_db(path=path)
    resp = {"path": path, "len": len(_impl_db._db)}
    return resp

@app.get("/add_to_db/{token}")
def add_to_db(token: str, q: Optional[str] = None):
    _impl_db.add_to_db(token=token)
    resp =  {"token": token, "len": len(_impl_db._db)}
    return resp

@app.get("/get_suggestions/{prefix}")
def read_item(prefix: str, limit: Optional[int] = 10):
    res = _impl_db.get_suggestions(prefix=prefix, limit=limit)
    resp = {"prefix": prefix, "limit": limit, "result": res}
    return resp


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


def main():
    uvicorn.run(app, host="0.0.0.0", port=18000)


if __name__ == "__main__":
    main()
