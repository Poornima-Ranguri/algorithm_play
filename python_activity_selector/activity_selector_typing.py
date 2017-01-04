#! /usr/bin/python
# activity_selector_typing
# David Branner
# 20170104

"""Pythonic versions of two illustrations of greedy algorithms.

After Cormen et al. (third edition), Section 16.1.

Here we avoid use of indices and cursors.

This version using the typing module, which causes Pytest to hang.
"""

from collections import deque
import sys
if sys.version_info < (3, 5):
    raise "Python version 3.5 or higher required for 'typing' module."

from typing import List, Tuple

def recursive(lst: List[Tuple[int, int]]=None) -> List[Tuple[int, int]]:
    """Identify greedy choice and then recurse on next possible list-tail.
    
    This is not a very interesting recursion.
    """
    # Empty case (not base case)
    if not lst:
        return list()
    # Ensure using deque within `recursive`, to enable popleft
    elif not isinstance(lst, deque):
        lst_d = deque(lst)

    # Function body begins here.
    greedy_choice = lst_d.popleft()
    to_return = deque([greedy_choice])
    while lst_d:
        if lst_d[0][0] >= greedy_choice[1]:
            returned = recursive(list(lst_d))
            if returned:
                to_return.extend(returned)
        else:
            lst_d.popleft()
    return list(to_return)

def iterative(lst: List[Tuple[int, int]]=None) -> List[Tuple[int, int]]:
    """Add 1st element, greedy choice; iteratively add possible successors."""
    # Empty case
    if not lst:
        return list()

    # Function body begins here.
    to_return = deque() # type: deque[Tuple[int, int]]
    for item in lst:
        if not to_return:
            to_return = deque([item]) # Initial greedy choice
        elif item[0] >= to_return[-1][1]:
            to_return.append(item)
    return list(to_return)
