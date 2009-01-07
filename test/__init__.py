# encoding: utf-8

import pymsl
from textwrap import dedent as _dedent

def dedent(s):
    return _dedent(s.strip("\r\n"))

def parses(code):
    try:
        pymsl.parse(code)
    except pymsl.ParseException, e:
        raise AssertionError(e)
    return True

def parses_not(code):
    try:
        pymsl.parse(code)
    except pymsl.ParseException:
        return True
    else:
        raise AssertionError("code should not have compiled")
