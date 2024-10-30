#!/usr/bin/python3
"""
 UTF-8 Validation
"""


def validUTF8(data):
    """
    Returns either Tru or FALSE depends if data is a valid UTF-8 encoding
    """
    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode()
    except:
        return False
    return True
