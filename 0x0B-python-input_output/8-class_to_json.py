#!/usr/bin/python3
"""Module that classes the json dictionay"""


def class_to_json(obj):
    """ function that returns the dictionary
    description
    """
    dic = {}
    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()
    return dic
