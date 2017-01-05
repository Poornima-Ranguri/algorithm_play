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

from typing import List, Tuple, MutableSequence

def recursive(dq: MutableSequence[Tuple[int, int]]=None) -> MutableSequence[Tuple[int, int]]:
    """Identify greedy choice and then recurse on next possible list-tail.
    
    This is not a very interesting recursion.
    """
    # Empty case (not base case)
    print('type(dq):', type(dq))
    if not dq:
        return deque()
    # Ensure using deque within `recursive`, to enable popleft#
#    elif not isinstance(lst, deque):
#        dq = deque(lst) # type: MutableSequence

    # Function body begins here.
    greedy_choice = dq.popleft() # type: Tuple
    to_return = deque([greedy_choice]) # type: MutableSequence
    while dq:
        if dq[0][0] >= greedy_choice[1]:
            print('recursing on', dq)
            returned = recursive(list(dq)) # type: List
            if returned:
                to_return.extend(returned)
        else:
            _ = dq.popleft()
#            print('current dq after else: {}; removed {}'.format(dq, _))
    return deque(to_return)

def iterative(dq: MutableSequence[Tuple[int, int]]=None) -> MutableSequence[Tuple[int, int]]:
    """Add 1st element, greedy choice; iteratively add possible successors."""
    # Empty case
    if not dq:
        return deque()

    # Function body begins here.
    to_return = deque() # type: deque[Tuple[int, int]]
    for item in dq:
        if not to_return:
            to_return = deque([item]) # Initial greedy choice
        elif item[0] >= to_return[-1][1]:
            to_return.append(item)
    return deque(to_return)
