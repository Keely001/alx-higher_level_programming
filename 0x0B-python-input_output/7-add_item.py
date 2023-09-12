#!/usr/bin/python3
""" script that adds all arguments to a Python list
and saves them to a file:"""
import sys
import os.path


load_from_json_file = \
    __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = \
    __import__('5-save_to_json_file').save_to_json_file
_list = []
if os.path.exists("add_item.json"):
    _list = load_from_json_file("add_item.json")
for arg in sys.argv[1:]:
    _list.append(arg)
save_to_json_file(_list, "add_item.json")