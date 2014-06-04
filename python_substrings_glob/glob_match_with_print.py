#! /usr/bin/env python
# glob_match_with_print.py
# David Prager Branner
# 20140603, works

"""Perform simple glob (global wildcard expansion) match on input string."""

from collections import deque

def main(p, s):
    """Use cursors, a queue, and memoization to match glob pattern to string."""
    print('This program describes the decisions that are being made at each step. For silent running, use `glob_match.py`.')
    # Populate initial variables.
    p_cursor = 0
    s_cursor = 0
    cursor_pair_queue = deque([(p_cursor, s_cursor)])
    cursor_pairs_seen = {}
    # Add non-wildcard elements of string to dictionary of actions.
    actions = {c: count_character for c in set(s)}
    actions['?'] = question_mark
    actions['*'] = star
    # Start traversing string and adding cursor-pairs to queue.
    while cursor_pair_queue:
        p_cursor, s_cursor = cursor_pair_queue.popleft()
        # Eliminate cursor-pairs already examined or having invalid s-cursor.
        if (p_cursor, s_cursor) in cursor_pairs_seen or s_cursor == len(s):
            continue
        else:
            cursor_pairs_seen[(p_cursor, s_cursor)] = True
        # Get next character of pattern
        if p_cursor < len(p):
            next_char = p[p_cursor]
        else:
            print('    Discard {} because p_cursor >= len(p).'.
                    format((p_cursor, s_cursor)))
            continue
        print('\n{}:{} ({}:{})'.
                format(p[p_cursor], s[s_cursor], p_cursor, s_cursor))
        # Compare character-pairs.
        try:
            print('    next action: {}'.format(actions[next_char].__name__))
            new_states = actions[next_char](p, s, p_cursor, s_cursor)
        except KeyError:
            print('''    Match has failed because character {} in pattern '''
                    '''is not in string'''.format(next_char))
            return False
        print('    on return, new states: {}'.format(new_states))
        if new_states:
            if s_cursor == len(s) - 1 and p_cursor == len(p) - 1:
                print('''    Match has succeed because s_cursor >= len(s) '''
                        '''{} >= {} and p_cursor == len(p) - 1: {} == {}.'''.
                        format(s_cursor, len(s) - 1, p_cursor, len(p) - 1))
                return True
            cursor_pair_queue.extend(new_states)
#        else:
#            print('''    Match has failed because character {} in pattern '''
#                    '''does not match character {} in string.'''.
#                    format(p[p_cursor], s[s_cursor]))
#            if not cursor_pair_queue:
#                return False
        print('    on return, queue: {}'.format(cursor_pair_queue))
    if s_cursor < len(s) - 1:
        print('''    Match has failed because pattern is not used up after '''
                '''cursor-pair queue is empty.''')
    if s_cursor > len(s) - 1:
        print('''    Match has failed because string is not used up after '''
                '''cursor-pair queue is empty.''')
    print('\ns_cursor:len(s)-1 {}:{}'.format(s_cursor, len(s) - 1))
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
