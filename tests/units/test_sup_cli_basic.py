def test__info():
    from searchup import sup_cli
    info_text = sup_cli.info(as_cli=False)
    assert 'Welcome' in info_text