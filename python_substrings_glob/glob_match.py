#! /usr/bin/env python
# glob_match.py
# David Prager Branner
# 20140603, works

"""Perform simple glob (global wildcard expansion) match on input string."""

from collections import deque

def main(p, s):
    # Populate initial variables.
    progress_messages = []
    p_cursor = 0
    s_cursor = 0
    the_queue = deque([(p_cursor, s_cursor)])
    cursor_pairs = {}
    # Add non-wildcard elements of string to dictionary of actions.
    actions = {c: count_character for c in set(s)}
    actions['?'] = question_mark
    actions['*'] = star
    # Start traversing string and adding cursor-pairs to queue.
    while the_queue:
        p_cursor, s_cursor = the_queue.popleft()
        # Eliminate cursor-pairs already examined and invalid s_cursor.
        if (p_cursor, s_cursor) in cursor_pairs or s_cursor == len(s):
            continue
        else:
            cursor_pairs[(p_cursor, s_cursor)] = True
        # Eliminate invalid p_cursor
        if p_cursor < len(p):
            next_char = p[p_cursor]
        else:
            continue
        # Try to match character-pairs.
        try:
            new_states = actions[next_char](p, s, p_cursor, s_cursor)
        except KeyError:
            return False
        if new_states:
            if s_cursor == len(s) - 1 and p_cursor == len(p) - 1:
                return True
            the_queue.extend(new_states)
        else:
            if not the_queue:
                return False
    return False

def count_character(p, s, p_cursor, s_cursor):
    """Advance cursors if exact match."""
    if p[p_cursor] == s[s_cursor]:
        return [(p_cursor + 1, s_cursor + 1)]

def question_mark(p, s, p_cursor, s_cursor):
    """Advance cursor on any character."""
    return [(p_cursor + 1, s_cursor + 1)]

def star(p, s, p_cursor, s_cursor):
    """Return three different cursor-pairs."""
    return [(p_cursor + 1, s_cursor),     # * matches 0 characters
            (p_cursor + 1, s_cursor + 1), # * matches 1 character
            (p_cursor, s_cursor + 1)      # * matches > 1 characters
            ]

if __name__ == '__main__':
    main()
