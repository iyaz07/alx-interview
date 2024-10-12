#!/usr/bin/python3
"""Python module to checks if all boxes can be opened
   from a list of lists
"""


def canUnlockAll(boxes=[]):
    """This function returns True if all box in
    boxes can be opend
    """
    if not boxes:
        return False

    keys = set([0])
    for box_id, box in enumerate(boxes):
        for key in box:
            if key < len(boxes) and key != box_id:
                keys.add(key)

    if len(keys) != len(boxes):
        return False

    return True
