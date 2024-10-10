#!/usr/bin/python3
"""
Module that provides a function to determine all boxes in a given list
"""


def canUnlockAll(boxes):
    """
    Determines whethe all boxes in the list can be opened
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        some_boxes = False
        for idx in range(len(boxes));
            some_boxes = k in boxes[idx] and k != idx
            if some_boxes:
                break
        if some_boxes is False:
            return some_boxes
    return True
