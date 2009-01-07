# encoding: utf-8

import math
from pymsl.identifiers import identifier

@identifier.const(float)
def pi():
    """

    >>> 3.14 < pi() < 3.15
    True

    """
    return math.pi

@identifier(float, property, returns=float)
def sin(n, deg=False):
    """Return the sine of N.

    >>> -1e-10 < sin(math.pi) < 1e-10
    True
    >>> 0.89 < sin(90) < 0.90
    True
    >>> sin(90, deg=True)
    1.0

    """
    if deg:
        n = math.radians(n)
    return math.sin(n)

@identifier(float, property, returns=float)
def cos(n, deg=False):
    """Return the cosine of N.

    >>> cos(math.pi)
    -1.0
    >>> -0.60 < cos(180) < -0.59
    True
    >>> cos(180, deg=True)
    -1.0

    """
    if deg:
        n = math.radians(n)
    return math.cos(n)
