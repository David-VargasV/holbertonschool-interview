#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
    """
    You have n number of locked boxes in
    front of you. Each box is numbered sequentially
    from 0 to n - 1 and each box may contain
    keys to the other boxes.
    """
    if type(boxes) is not list or not all(type(box) is list for box in boxes):
        return False

    l_Box = len(boxes)

    if l_Box == 0:
        return False

    if l_Box == 1:
        return True

    if not boxes[0] and l_Box > 1:
        return False

    unlock = {k: False for k in range(l_Box)}

    unlock[0] = True

    keys = [key for key in boxes[0]]

    while keys:
        n_key = []
        for key in keys:
            if key in unlock.keys() and unlock[key] is False:
                n_key += boxes[key]
                unlock[key] = True

        if all(unlock.values()) and len(unlock) == l_Box:
            return True

        keys = n_key
    return False
