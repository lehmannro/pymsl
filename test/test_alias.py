# encoding: utf-8

import pymsl.test as test

def test_empty():
    assert test.parses("")

def test_alias_declaration():
    tests = (s.split(None, 1) for s in test.dedent("""
    0 alia
    0 alias
    1 alias a
    1 alias a { }
    0 alias a{ }
    0 alias a {}
    1 alias a  { }
    0 alias a {
    1 alias a bar
    1 alias a $bar
    """).splitlines())
    #alias a {echo b } works indeed!
    #alias a {} should work but is useless.
    for success, code in tests:
        yield (test.parses, test.parses_not)[success == "0"], code
