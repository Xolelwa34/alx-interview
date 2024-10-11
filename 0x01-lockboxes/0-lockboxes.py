#!/usr/bin/python3
"""
Module that provides a function to determine all boxes in a given list
"""


def canUnlockAll(boxes):
    """
    Return True if can be open, false if not
    """
    number_of_keys = [0]
    number_of_boxes = len(boxes)

    for keys in number_of_keys:
        for box in boxes[keys]:
            if box < number_of_boxes and box not in number_of_keys:
                number_of_keys.append(box)
    if len(number_of_keys) == number_of_boxes:
        return True
    return False
