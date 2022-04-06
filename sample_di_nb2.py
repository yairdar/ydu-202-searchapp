# %% [markdown]
# ## Yeild All
# %%
input_data = {
    'a': {
        'g' : {3 :"This is terminator won't show up"},
        'z' : {17:2, "[deep]": {"[some]": "[fine]", "[stuff]": 0}, 16:36},
        't' : ''
    },
    'b': {
        't': 0,
        'a': {'r': 0}
    }
}    

class DPrinter:
    def __init__(self, d: dict) -> None:
        self.itor = iter(d.items())
        
    def next(self, default=NotImplemented):
        item = next(self.itor, default)
        return item
    
class DictWalker:
    def __init__(self, d: dict) -> None:
        self.start = d
        # iterators bag
        self.iters_stack = [DPrinter(self.start)]
        self.path_chars = []
        
    def next(self):
        if len(self.iters_stack) == 0:
            return NotImplemented
        
        item = NotImplemented
        while item is NotImplemented:
            # take next item from stack
            
            item = self.iters_stack[-1].next(NotImplemented)
            
             # keep trying  totake  next item from iteratros stack
            if item is NotImplemented:
                self.iters_stack.pop()
                if self.path_chars:
                    self.path_chars.pop()
                if len(self.iters_stack) == 0:
                    return NotImplemented
                
        key, value = item 

        if isinstance(value, dict):
            self.iters_stack.append(DPrinter(value))
            self.path_chars.append(key)
        return item
    
    def iter_path(self, *args):
        for c in self.path_chars:
            yield c
        for c in args:
            yield c
    
    def iter(self):
        while True:
            item = self.next()
            if item is NotImplemented:
                break
            key, val = item
            if not isinstance(val, dict):
                yield "".join([str(c) for c in self.iter_path(key)])

def test_dict_walker():             
    dp_walker = DictWalker(input_data)
    for it in dp_walker.iter():
        print(it)                
test_dict_walker()
