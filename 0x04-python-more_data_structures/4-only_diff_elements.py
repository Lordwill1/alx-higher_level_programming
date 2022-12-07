#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    A function that returns a set of all elements
    present in only one set.
    """
    return (set_1 ^ set_2)
