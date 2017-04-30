import sys
if sys.version_info < (3, 5):
    raise "Python version 3.5 or higher required for 'typing' module."

import typing

def sample_odd_first(n: int) -> int:
    """Set a variable one of two different ways, depending on input"""
    if n % 2:
       x = 1 # type: int
    else:
       x = 0 # type: int
    return x

def sample_even_first(n: int) -> int:
    """Set a variable one of two different ways, depending on input"""
    if not (n % 2):
       x = 0 # type: int
    else:
       x = 1 # type: int
    return x
