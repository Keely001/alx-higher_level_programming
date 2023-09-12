#!/usr/bin/python3
""" script that adds all arguments to a python list"""
import sys
import os


load_f = \
    __import__('6-load_from_json_file').load_from_json_file
save = \
    __import__('5-save_to_json_file').save_to_json_file
m_list = []
if os.path.exists("add_item.json"):
    m_list = load_f("add_item.json")
for arg in sys.argv[1:]:
    m_list.append(arg)
save(m_list, "add_item.json")
