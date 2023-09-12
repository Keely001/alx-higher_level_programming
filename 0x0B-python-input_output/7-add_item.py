#!/usr/bin/python3
""" a script that adds all arguments to a Python list"""
import sys
import os.path


load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

_list = []
if os.path.exists("add_item.json"):
    _list = load("add_item.json")
for arg in sys.argv[1:]:
    _list.append(arg)
save(_list, "add_item.json")
