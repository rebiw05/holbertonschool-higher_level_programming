#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import os


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML format and saves it to a file.

    Args:
        dictionary (dict): The Python dictionary to serialize.
        filename (str): The name of the file to save the XML data to.
    """
    # Create the root element for the XML document
    root = ET.Element("data")

    # Iterate through the dictionary items
    for key, value in dictionary.items():
        # Create a child element for each key-value pair
        # The key becomes the tag name, and the value becomes the text content
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create an ElementTree object from the root element
    tree = ET.ElementTree(root)

    # Indent the XML for better readability (pretty-printing)
    # This function is available from Python 3.9+
    ET.indent(tree, space="    ")

    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Reads XML data from a file and deserializes it into a Python dictionary.

    Args:
        filename (str): The name of the XML file to read from.

    Returns:
        dict: The deserialized Python dictionary.
              Returns an empty dictionary if the file is not found or empty.
    """
    deserialized_dict = {}
    try:
        # Parse the XML file to get the ElementTree object
        tree = ET.parse(filename)
        # Get the root element of the XML tree
        root = tree.getroot()

        # Iterate through the child elements of the root
        for child in root:
            # The tag of the child element becomes the key in the dictionary
            # The text content of the child element becomes the value
            deserialized_dict[child.tag] = child.text

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ET.ParseError as e:
        print(f"Error parsing XML file '{filename}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return deserialized_dict


if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',  # Stored as string as per example output
        'city': 'New York'
    }

    xml_file = "data.xml"

    # Test serialization
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    # Test deserialization
    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)
