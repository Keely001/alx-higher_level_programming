#!/usr/bin/python3
""" unittest for base class """

import unittest
from io import StringIO
import os
from models.base import Base
from models.square import Square
from unittest.mock import patch
from unittest import TestCase
from models.rectangle import Rectangle


class TestBaseMethods(unittest.TestCase):
    """ test the Base class """

    def setUp(self):
        """ for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test for assigned  id """
        nw = Base(1)
        self.assertEqual(nw.id, 1)

    def test_id_d(self):
        """ Test for default id """
        nw = Base()
        self.assertEqual(nw.id, 1)

    def test_no_arg(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_id_m(self):
        """ Test object attributes and assigned id """
        nw1 = Base()
        nw2 = Base()
        nw3 = Base(1024)
        self.assertEqual(nw1.id, 1)
        self.assertEqual(nw2.id, 2)
        self.assertEqual(nw3.id, 1024)

    def test_tuple_id(self):
        self.assertEqual((3, 2), Base((3, 2)).id)

    def test_list_id(self):
        self.assertEqual([8, 4, 3], Base([8, 4, 3]).id)

    def test_str_id(self):
        """ test if """
        new = Base('1')
        self.assertEqual(new.id, '1')
        
    def test_set_id(self):
        self.assertEqual({6, 2, 3}, Base({6, 2, 3}).id)

    def test_mo_args_id(self):
        """ test for args """
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_to_json_string_rect_one_dict(self):
        rec = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([rec.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        rec1 = Rectangle(2, 3, 5, 19, 2)
        rec2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [rec1.to_dictionary(), rec2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_sq_type(self):
        sq = Square(1, 2, 30, 4)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))

    def test_to_json_string_sq(self):
        sq = Square(1, 2, 30, 4)
        self.assertTrue(len(Base.to_json_string([sq.to_dictionary()])) == 39)

    def test_save_to_file_two_rec(self):
        rec1 = Rectangle(10, 7, 2, 8, 5)
        rec2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rec1, rec2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_a_sq(self):
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_load_from_file_square_type(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sq1, sq2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        outp = Square.load_from_file_csv()
        self.assertEqual([], outp)


if __name__ == "__main__":
    unittest.main()