# encoding: utf-8

import locale
import math
import string
from pymsl.identifiers import identifier
locale.setlocale(locale.LC_ALL, '')

@identifier(str, returns=int)
def asc(c):
    """Returns the ASCII number of the character C.

    >>> asc("A")
    65
    >>> asc("*")
    42

    """
    return ord(c[0])

@identifier(int, str, property, returns=str)
def bytes(n, options, suf=False):
    """Returns comma formatted filesize.

    >>> print bytes(1000, "b")
    1,000
    >>> print bytes(1024, "k")
    1
    >>> print bytes(1000, "k")
    0.98
    >>> print bytes(10000000, "k") # mIRC yields 9,765.63
    9,765.62
    >>> print bytes(1, "k")
    0
    >>> print bytes(1024**2, "m")
    1
    >>> print bytes(1, "b", suf=True)
    1B
    >>> print bytes(1, "k", suf=True)
    0KB
    >>> print bytes(1, "3")
    1
    >>> print bytes(1024, "3")
    1

    """
    if options == "3":
        exponent = int(math.log(n, 1024)) #XXX
    else:
        exponent = "bkmgt".index(options)
    n = n / (1.0 * 1024**exponent)
    result = locale.format('%3.2f', n, True)
    if result.endswith(".00"):
        result = result.rstrip("0")[:-1] #XXX 1.00, 10.0, 100
    if suf:
        result += "BKMGT"[exponent]
        if exponent:
            result += "B"
    return result

@identifier(int, returns=str)
def chr_(n):
    """Returns the character with ASCII number N.

    >>> chr_(65)
    'A'
    >>> chr_(42)
    '*'

    """
    return chr(n)

@identifier(str, int, returns=str)
def str_(text, n):
    """Returns text repeated N times.

    >>> print str_("ho", 3)
    hohoho

    """
    return text * n

@identifier(str, str, returns=int)
def count(string, *substrings):
    """Returns the number of times substring occurs in string.

    >>> count("hello", "el")
    1
    >>> count("hello", "l")
    2
    >>> count("hello", "l", "l")
    4
    >>> count("ababa", "aba")
    1

    """
    return sum(string.count(substring) for substring in substrings)

@identifier(str, returns=int)
def len_(text):
    """Returns the length of text.

    >>> len("#mIRC")
    5

    """
    return len(text)

@identifier(str, returns=bool)
def islower(text):
    """Returns True if text is all lower case.

    >>> islower("abc")
    True
    >>> islower("abC")
    False
    >>> islower("") == None
    True
    >>> islower("abc_")
    True
    >>> islower("_")
    True
    >>> islower("ü")
    True
    >>> islower("Ü")
    True

    """
    if not text:
        return None
    return not any(chr(nchar) in text for nchar in xrange(ord("A"), ord("Z")+1))

@identifier(str, returns=bool)
def isupper(text):
    """Returns True if text is all upper case.

    >>> isupper("ABC")
    True
    >>> isupper("ABc")
    False
    >>> isupper("") == None
    True
    >>> isupper("ABC_")
    True
    >>> isupper("_")
    True
    >>> isupper("ü")
    True
    >>> isupper("Ü")
    True

    """
    if not text:
        return None
    return not any(chr(nchar) in text for nchar in xrange(ord("a"), ord("z")+1))

@identifier(str, int, int, int, int, returns=str)
def base(n, inbase, outbase, zeropad=0, precision=0):
    """Converts number N from inbase to outbase.

    >>> print base('dead', 16, 10)
    57005
    >>> print base('4', 10, 2, 1)
    100
    >>> print base('4', 10, 2, 5)
    00100

    >>> print base('15', 10, 16)
    F
    >>> print base('1.5', 10, 16) # doctest: +SKIP
    1.8
    >>> print base('2', 10, 16, 3)
    002

    """ #XXX floats, precision
    if inbase > 36 or outbase > 36:
        return False
    return _itoa(_atoi(n, inbase), outbase).zfill(zeropad)

_digits = string.digits + string.uppercase
def _itoa(n, base, trans=_digits):
    """Return the string representing the integer `n` in the given base.

    >>> print _itoa(16, 10)
    16
    >>> print _itoa(16, 2)
    10000
    >>> print _itoa(16, 16)
    10
    >>> print _itoa(15, 16)
    F
    >>> print _itoa(35, 36)
    Z
    >>> print _itoa(36, 37) # doctest: +ELLIPSIS
    Traceback (most recent call last):
      ...
    IndexError: ...

    """
    return (n and _itoa(n // base, base) + _digits[n % base] or '')

def _atoi(a, base, trans=_digits):
    """Return the integer represented by the string `a` in the given base.

    >>> _atoi("F", 16)
    15
    >>> _atoi("10", 2)
    2
    >>> _atoi("B", 10) # out of bounds, actually
    11

    """ #XXX doctests
    return sum(base**pos * trans.index(val)
           for pos, val in enumerate(reversed(a.upper())))
