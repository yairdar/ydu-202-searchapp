# internal methods:

def init_db():
    return {}


def add_to_db(mdb:dict, token:str):
    token_added = False
    cur = mdb
    for char in token:
        if char not in cur:
            cur[char] = {}
        cur = cur[char]
    if not None in cur:
        cur[None] = None
        token_added = True
    return token_added

"""
O(n) where n is a token length
"""

# return bool
# if this token is already in the db, it doesn't get added and add_to_db() returns False
# if token is added, add_to_db() returns True

def iterable_tokens(path:str):
    with open(path, 'r') as f_tokens:
        db_tokens = []
        for line in f_tokens:
            if line.endswith('\n'):
                token = line[0:-1]
            else:
                token = line
            yield token
        return db_tokens

# return iterable[str]

"""
O(n) where n is a number of tokens
"""


def find_prefix(mdb:dict, prefix:str):
    cur = mdb
    for char in prefix:
        if char in cur:
            cur = cur[char]
        else:
            return None
    return cur

"""
O(n) where n is a number of characters in a prefix
"""
    
# return dict
# start from root mdb and returns root for end of prefix


# iterative implementation of trie traversal with a branch buffer

def iterate_suffixes(mdb: dict):
    suffixes = []
    branch_buffer = {}

    suffix = []
    cur = mdb

    while cur:
        # when we reach the suffix end
        if cur == {None: None}:
            # we turn the suffix into a string then yield it
            yield ''.join(suffix)
            # if branch buffer is not empty
            # we extract the last added path to the branch and the branching node's children iterator from the buffer
            if branch_buffer:
                branch_path, branch_children = branch_buffer.popitem()
                # when the iterator over node's children gets exhausted it will return NotImplements as a marker
                child = next(branch_children, NotImplemented)

                # if child == None, the branch_path is a complete suffix itself, and we yield it now
                if child == None:
                    yield branch_path
                    child = next(branch_children, NotImplemented)

                # if the branch_children iterator is exhausted
                while child == NotImplemented:
                    # and there is something in the branch_buffer
                    if branch_buffer:
                        # we pop the last item from the branch buffer
                        branch_path, branch_children = branch_buffer.popitem()
                        # get the current child and check once again, maybe this branch_children iterator is exhausted too
                        child = next(branch_children, NotImplemented)
                    else:
                        break

                # if the iterator have already got exhausted on previous steps, we don't return it to the branch buffer
                # we must break from branch_buffer processing here to prevent passing NotImplemented as a key to the cur
                if child == NotImplemented:
                    break
                else:
                    branch_buffer[branch_path] = branch_children

                # here we step through all the branch path chars down the sub-trie to get to the branching node
                # also we convert the branch_path to the beginning of the suffix
                # suffix is a list, not a string, to speed up appending characters to it
                cur = mdb
                suffix = []
                for char in branch_path:
                    cur = cur[char]
                    suffix.append(char)

                # and here we switch to the current branch
                if child == None:
                    cur = {None: None}
                else:
                    suffix.append(child)
                    cur = cur[child]
            # to prevent an infinite loop if the branch buffer is empty
            else:
                break

        # the keys of the cur are the children of the current node, and we get an iterator over them
        children = iter(cur.keys())
        children_count = len(cur.keys())
        child = next(children)

        # if cursor meets branch, it writes the node information to the buffer
        # suffix serves as a path to the node in a trie and children is the node children iterator
        if children_count > 1:
            branch_path = ''.join(suffix)
            branch_buffer[branch_path] = children
        if child == None:
            cur = {None:None}
        else:
            suffix.append(child)
            cur = cur[child]

    return suffixes

    # return iterable[str]


def retrive_suffixes_by_prefix(mdb:dict, prefix:str, limit:int=10):
    subtrie = find_prefix(mdb=mdb, prefix=prefix)
    if subtrie:
        itsuf = iterate_suffixes(subtrie)
        if not limit:
            suffixes = [suf for suf in itsuf]
        else:
            suffixes = []
            for suf in itsuf:
                suffixes.append(suf)
                limit -= 1
                if limit == 0:
                    return suffixes
        return suffixes
    else:
        return None

    # return list[str]

# external API methods:

def load_db(path:str=None):
    mdb = init_db()
    if path:
        itokens = iterable_tokens(path=path)
        for itoken in itokens:
            add_to_db(mdb=mdb, token=itoken)
    return mdb


def get_suggestions(mdb:dict, prefix:str, limit:int=10):
    suffixes = retrive_suffixes_by_prefix(mdb=mdb, prefix=prefix, limit=limit)
    if suffixes:
        suggestions = [prefix + suffix for suffix in suffixes]
        return suggestions
    else:
        return []