#! /usr/bin/python
# activity_selector
# David Branner
# 20170105

""""""

import sys
if sys.version_info < (3, 5):
    raise "Python version 3.5 or higher required for 'typing' module."

from typing import Callable

def sample_odd_first(n: int) -> Callable[[], int]:
    """Set a variable one of two different ways, depending on input"""
    if n % 2:
       def fn() -> int:
           x = 1 # type: int
           return x
    else:
       def fn() -> int:
           x = 0 # type: int
           return x
    return fn

def sample_even_first(n: int) -> Callable[[], int]:
    """Set a variable one of two different ways, depending on input"""
    if not (n % 2):
       def fn() -> int:
           x = 0 # type: int
           return x
    else:
       def fn() -> int:
           x = 1 # type: int
           return x
    return fn
