#!/usr/bin/python3
"""determine if all boxes can be opened"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    
    Args:
    - boxes: a list of lists where each index represents a box number
             and the value at that index is a list of keys inside that box
    
    Returns:
    - True if all boxes can be opened, else False
    """
    if not boxes:
        return False
    
    n = len(boxes)
    keys = [0]
    visited = [False] * n
    visited[0] = True
    
    while keys:
        current_key = keys.pop()
        current_box = boxes[current_key]
        
        for key in current_box:
            if 0 <= key < n and not visited[key]:
                keys.append(key)
                visited[key] = True
    
    return all(visited)
