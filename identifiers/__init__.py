# encoding: utf-8

import functools
import inspect
import re

all = {}

defaults = dict(returns=str, const=False, alias=None)
def identifier(*args, **kwargs):
    args = list(args)
    options = defaults.copy()
    options.update(kwargs)
    if args and isinstance(args[0], str):
        options['name'] = args.pop(0)
    def deco(func):
        pargs, varargs, varkw, defaults = inspect.getargspec(func)
        func.return_annotation = kwargs
        # register
        name = options.get('name', func.__name__)
        #XXX check for name
        all[name] = func
        #XXX add mirc interface (str-only call)
        return func
    return deco

identifier.const = lambda typ, **kwargs:identifier(const=True, returns=typ, **kwargs)
