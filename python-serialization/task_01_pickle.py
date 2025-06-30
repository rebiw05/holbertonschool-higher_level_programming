#!/usr/bin/python3
"""
this is module
"""


import pickle


class CustomObject:
    """
    A custom class to represent an object with a name, age, and student status.

    Attributes:
        name (str): The name of the object.
        age (int): The age of the object.
        is_student (bool): A boolean indicating if the object is a student.
    """

    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initializes a new CustomObject instance.

        Args:
            name (str): The name to be assigned to the object.
            age (int): The age to be assigned to the object.
            is_student (bool): The student status to be assigned to the object.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the attributes of the CustomObject instance.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        """
        Serializes the current instance of CustomObject
        to a file using the pickle module.

        Args:
            filename (str): The name of the file
            saving the serialized object to.
        """
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename: str):
        """
        Deserializes a CustomObject instance from
        file using the pickle module.
        This is a class method,
        so it can be called directly on the class.

        Args:
            filename (str): The name of the file
            to load the serialized object from.
        """
        with open(filename, "rb") as file:
            return pickle.load(file)
