#!/usr/bin/python3
"""
File Input Output Module
"""
import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”:
    """
    with open(filename, "r") as json_file:
        return json.load(json_file)
