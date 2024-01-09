#!/usr/bin/python3
"""
determine if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    Args:
    - boxes: a list of lists where each index represents a box number
    Returns:
    - True if all boxes can be opened, else False
    """
    if not boxes or type(boxes) is not list:
        return False

    opened = [0]
    for n in opened:
        for key in boxes[n]:
            if key not in opened and key < len(boxes):
                opened.append(key)
    if len(opened) == len(boxes):
        return True
    return False
