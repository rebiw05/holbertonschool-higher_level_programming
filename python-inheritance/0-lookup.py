def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect. This can be an instance of a class,
             a class itself, or any other Python object (e.g., int, str).

    Returns:
        A list of strings, where each string is the name of an attribute
        or method available for the given object. The list is typically
        sorted alphabetically.
        """
    return dir(obj)
