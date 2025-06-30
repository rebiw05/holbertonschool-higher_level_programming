#!/usr/bin/python3
"""
this module serialize using xml
"""


import xml.etree.ElementTree as ET
"""
this is library
"""


import json
"""
this is library
"""

def serialize_to_xml(dictionary, filename):
    """
    this is function
    """
    root = ET.Element("data")
    name = ET.SubElement(root, "name")
    name.text = sample_dict["name"]
    age = ET.SubElement(root, "age")
    age.text = sample_dict["age"]
    city = ET.SubElement(root, "city")
    city.text = sample_dict["city"]
    tree = ET.ElementTree(root)
    tree.write("data.xml", encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """
    this is function
    """
    tree = ET.parse("data.xml")
    root = tree.getroot()
    for element in root:
        if element.tag == "name":
            sample_dict_new["name"] = element.text
        elif element.tag == "age":
            sample_dict_new["age"] = int(element.text)
        elif element.tag == "city":
            sample_dict_new["city"] = element.text
