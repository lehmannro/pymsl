#!/usr/bin/env python
# encoding: utf-8
# 
# 

import functools
from pyparsing import *

#TODO ignore / in ALIASDECL and ALIASCALL
#     alias /foo == alias foo
#     $/foo == $foo (even if declared by ``alias foo``)

AliasName = Word(alphanums + alphas8bit + punc8bit
                 + r"""!"#$%&'*+-./:<=>?@\^_`~""")
#FIXME r",;[]{|}"

Suite = (
          Suppress("{")
          #XXX
        + White(" ")
        + Suppress("}")
        )

Alias = (
          Suppress(CaselessLiteral("alias")) #XXX keyword?
        + Optional(Keyword("-l"))('LOCAL')
        + AliasName
        + Optional(White(" ") + Suite)
        )('ALIASDECL')
Script = ZeroOrMore(Alias) | empty

parse = functools.partial(Script.parseString, parseAll=True)
