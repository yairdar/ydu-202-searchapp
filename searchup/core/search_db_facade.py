""" Provides unified API for different search db implementations
"""


class DbFacade:
    """Adapter Class to underliyng actual implementation 
    currently we hardcoded djfedeos implementation from https://github.com/djfedos/djfedos-search
    """
    
    def __init__(self) -> None:
        import lib_search_sdk
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
  