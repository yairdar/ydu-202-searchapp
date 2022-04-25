"""
This is the set of unit test. It tests the behavior of each function in lib_test_sdk.py
"""


import lib_search_sdk
from pathlib import Path

_me_parent = Path(__file__).absolute().parent


def test_init_db():
    #arrange
    expected_db = {}
    #act
    actual_db = lib_search_sdk.init_db()

    assert expected_db == actual_db


def test_add_to_db():
    #arrange
    empty_db = {}
    not_empty_db = {'m': {'a': {'y': {'a': {None: None}, None: None}, 'n': {None: None}}}}
    expected_empty_db = {'m':{'a':{'n':{None:None}}}}
    token = 'man'
    #act
    added_to_empty_db = lib_search_sdk.add_to_db(empty_db, token)
    added_to_not_empty_db = lib_search_sdk.add_to_db(not_empty_db, token)

    assert empty_db == expected_empty_db
    assert added_to_empty_db
    assert not added_to_not_empty_db


def test_iterable_tokens():
    #arrange
    token_path = f'{_me_parent}/tests/tokens.txt'
    expected_tokens = {'marsaba', 'maramba', 'man', 'may', 'bar', 'baron', 'banya', 'raba', 'rab'}
    #act
    tokens = lib_search_sdk.iterable_tokens(token_path)
    actual_tokens = {token for token in tokens}
    assert actual_tokens == expected_tokens


def test_find_prefix():
    #arrange
    expected_not_found = None
    expected_subtrie = {'b':{'a':{None:None}, None:None}}
    prefix = 'ra'
    prefix_not_in_mdb = 'ly'
    token_path = f'{_me_parent}/tests/tokens.txt'
    mdb = lib_search_sdk.load_db(token_path)
    #act
    actual_subtrie = lib_search_sdk.find_prefix(mdb, prefix)
    actual_not_found = lib_search_sdk.find_prefix(mdb, prefix_not_in_mdb)

    assert actual_subtrie == expected_subtrie
    assert actual_not_found == expected_not_found


def test_iterate_suffixes_short():
    #arrange
    expected_suffixes = {'b', 'ba'}
    mdb = {'b': {'a': {None: None}, None: None}}
    #act
    suffixes = lib_search_sdk.iterate_suffixes(mdb)
    actual_suffixes = {suffix for suffix in suffixes}

    assert actual_suffixes == expected_suffixes


def test_iterate_suffixes_mid():
    #arrange
    expected_suffixes = {'may', 'maya', 'man'}
    mdb = {'m': {'a': {'y': {'a': {None: None}, None: None}, 'n': {None: None}}}}
    #act
    suffixes = lib_search_sdk.iterate_suffixes(mdb)
    actual_suffixes = {suffix for suffix in suffixes}

    assert actual_suffixes == expected_suffixes


def test_retrive_suffixes_by_prefix():
    #arrange
    token_path = f'{_me_parent}/tests/tokens.txt'
    mdb = lib_search_sdk.load_db(token_path)
    prefix = 'ra'
    prefix_not_in_mdb = 'ly'
    expected_suffixes_unlim = {'b', 'ba'}
    expected_suffixes_lim = {'ba'}
    expected_suffixes_high_lim = {'b', 'ba'}
    limit = 1
    high_limit = 12
    #act
    actual_suffixes_unlim = set(lib_search_sdk.retrive_suffixes_by_prefix(mdb, prefix))
    actual_suffixes_lim = set(lib_search_sdk.retrive_suffixes_by_prefix(mdb, prefix, limit))
    actual_suffixes_high_lim = set(lib_search_sdk.retrive_suffixes_by_prefix(mdb, prefix, high_limit))
    actual_suffixes_not_found = lib_search_sdk.retrive_suffixes_by_prefix(mdb,prefix_not_in_mdb)

    assert actual_suffixes_unlim == expected_suffixes_unlim
    assert actual_suffixes_lim == expected_suffixes_lim
    assert actual_suffixes_high_lim == expected_suffixes_high_lim
    assert not actual_suffixes_not_found


def test_load_db():
    #arrange
    expected_db = {'m':{'a': {'r': {'s': {'a': {'b': {'a': {None: None}}}}, 'a': {'m': {'b': {'a': {None: None}}}}},
                    'n': {None: None}, 'y': {None: None}}}, 'b': {'a': {'r': {None: None, 'o': {'n': {None: None}}},
                    'n': {'y': {'a': {None: None}}}}}, 'r': {'a': {'b': {'a': {None: None}, None: None}}}}
    token_path = f'{_me_parent}/tests/tokens.txt'
    #act
    actual_db = lib_search_sdk.load_db(token_path)

    assert actual_db == expected_db


def test_get_suggestions():
    #arrange
    token_path = f'{_me_parent}/tests/tokens.txt'
    mdb = lib_search_sdk.load_db(token_path)
    prefix = 'ma'
    prefix_not_found = 'ly'
    limit = 2
    expected_suggestions_unlim = {'marsaba', 'maramba', 'man', 'may'}
    expected_suggestions_not_found = []
    #act
    actual_suggestions_unlim = set(lib_search_sdk.get_suggestions(mdb, prefix))
    actual_suggestions_lim = lib_search_sdk.get_suggestions(mdb, prefix, limit)
    actual_suggestions_not_found = lib_search_sdk.get_suggestions(mdb, prefix_not_found)

    assert actual_suggestions_unlim == expected_suggestions_unlim
    assert len(actual_suggestions_lim) == 2
    assert actual_suggestions_lim[0] in expected_suggestions_unlim
    assert actual_suggestions_lim[1] in expected_suggestions_unlim
    assert actual_suggestions_not_found == expected_suggestions_not_found


def test_dump_db():
    #arrange
    dump_path = 'mdb_dump'  # this is the default dump path, but you may pass any other one if you wish, see next test
    token_path = f'{_me_parent}/tests/tokens.txt'
    mdb = lib_search_sdk.load_db(token_path)
    expected_file_content = {'marsaba', 'maramba', 'man', 'may', 'bar', 'baron', 'banya', 'raba', 'rab'}
    #act
    lib_search_sdk.dump_db(mdb)
    dump_file_name = '/token_db.txt'
    full_path = dump_path + dump_file_name
    actual_file_content = set()
    with open(full_path, 'r') as dump_file:
        for line in dump_file:
            line = line.strip()
            actual_file_content.add(line)

    assert actual_file_content == expected_file_content


def test_dump_db_custom_path():
    #arrange
    dump_path = 'my_db_dump'  # this is a custom dump path
    token_path = f'{_me_parent}/tests/tokens.txt'
    mdb = lib_search_sdk.load_db(token_path)
    expected_file_content = {'marsaba', 'maramba', 'man', 'may', 'bar', 'baron', 'banya', 'raba', 'rab'}
    #act
    lib_search_sdk.dump_db(mdb, dump_path)  # note the second argument with a custom path
    dump_file_name = '/token_db.txt'
    full_path = dump_path + dump_file_name
    actual_file_content = set()
    with open(full_path, 'r') as dump_file:
        for line in dump_file:
            line = line.strip()
            actual_file_content.add(line)

    assert actual_file_content == expected_file_content

"""
this feature is disabled and the test os disabled too

def test_add_to_db_dumps():
    #arrange
    mdb = lib_search_sdk.load_db()
    test_token = 'testtoken'
    dump_file_path = 'mdb_dump/token_db.txt'
    #act
    lib_search_sdk.add_to_db(mdb, test_token)
    actual_file_content = set()
    with open(dump_file_path, 'r') as dump_file:
        for line in dump_file:
            line = line.strip()
            actual_file_content.add(line)

    assert test_token in actual_file_content
"""