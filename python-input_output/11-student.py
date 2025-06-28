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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of strings specifying
                                    which attributes to retrieve.
                                    If None or not a list of strings,
                                    all attributes will be retrieved.

        Returns:
            dict: A dictionary containing the specified (or all)
                  public instance attributes of the Student.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            # If attrs is a list of strings, return only those attributes
            # that exist in the instance's dictionary.
            return {
                key: getattr(self, key)
                for key in attrs if hasattr(self, key)
            }
        else:
            # Otherwise, return all attributes of the object instance.
            return self.__dict__

    def reload_from_json(self, json):
        """
        Args:
            json (dict): A dictionary where keys are attribute names
                         and values are the corresponding attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
