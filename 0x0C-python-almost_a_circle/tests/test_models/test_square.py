#!/usr/bin/python3

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(10, 10, 10, 10)
    def tearDown(self):
        del self.square
    def test_initialisation_and_str(self):
        self.assertEqual(str(self.square), "[Square] (10) 10/10 - 10")
    def test_area(self):
        self.assertEqual(self.square.area(), 100)
