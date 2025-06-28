#!/usr/bin/python3
"""
9-student.py

This module defines the Student class.
"""


class Student:
    """Defines a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing the public instance attributes
                  (first_name, last_name, age) of the Student.
        """
        return self.__dict__
