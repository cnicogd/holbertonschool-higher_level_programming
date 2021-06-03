#!/usr/bin/python3
"""returns a list from a module"""


class MyList(list):
    """
    Class Mylist inherits list
    """

    def print_sorted(self):
        """
        prints the list, but sorted
        """
        print(sorted(self))
