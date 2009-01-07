# encoding: utf-8

from pymsl.identifiers import identifier

@identifier('abs', int, returns=int)
def m_abs(n):
    """Returns the absolute value of number N.

    >>> m_abs(5)
    5
    >>> m_abs(-1)
    1

    """
    return abs(n)

@identifier(float, returns=int)
def ceil(n):
    """Returns N rounded to the next highest integer.

    >>> ceil(5.5)
    6
    >>> ceil(1.0)
    1

    """
    if (n % 1) == 0: #XXX < 1e-N
        return int(n)
    return int(n + 1)

# According to mIRC's math implementation, the following should be valid:
# 
# >>> ceil(999999999999999)
# 999999999999999
# >>> ceil(9999999999999999)
# 9999999999999998
# >>> ceil(99999999999999999)
# 100000000000000000
# 
# >>> ceil(9999999999999998977)
# 10000000000000000000
# >>> ceil(9999999999999998976)
# 9999999999999998000
# 
# >>> ceil(55555555555555555)
# 55555555555555552
# >>> ceil(55555555555555550)
# 55555555555555552
# >>> ceil(55555555555555556)
# 55555555555555552
# >>> ceil(55555555555555557)
# 55555555555555560
# 
# >>> ceil(decimal("1.0000000000000001110"))
# 1
# >>> ceil(decimal("1.0000000000000001111"))
# 2
# >>> ceil(decimal("1e-323") # $ceil($+(0.,$str(0,322),1)
# 1
# >>> ceil(decimal("1e-324") # $ceil($+(0.,$str(0,323),1)
# 0
# 
# The same can be reproduced with a bare ``$calc`` in mIRC for all integers.
