#!/usr/bin/python3
class MyList(list):
    """
    A class MyList that inherits from the built-in list class.

    This class extends the functionality of a standard Python list by adding
    a new method to print its elements in ascending sorted order without
    modifying the original list.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.

        This method creates a new sorted version of the list and prints it.
        It does not modify the original list instance.

        Assumes all elements in the list are of type int.

        """
        sorted_list = sorted(self)
        print(sorted_list)
