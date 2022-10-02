import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    
    def setUp(self):
        rec = Rectangle(1, 1, 0, 0, 1)

    def tearDown(self):
        rec = None
        del rec

    def test_id_is_None(self):
        rec = Rectangle(2, 1)
        self.assertEqual(rec.id, 1)

    def test_id_not_None(self):
        rec = Rectangle(12, 8, 0, 0, 4)
        self.assertEqual(rec.id, 4)

    def test_invalid_width(self):
        rec = Rectangle(-8, 3)
        self.assertRaises(ValueError, msg="width must be > 0")

    def test_invalid_height(self):
        rec = Rectangle(10, -4)
        self.assertRaises(ValueError, msg="height must be > 0")

    def test_if_width_is_integer(self):
        rec = Rectangle("ten", 4)
        self.assertRaises(TypeError, msg="width must be an integer")

    def test_if_height_is_integer(self):
        rec = Rectangle(10, "four")
        self.assertRaises(TypeError, msg="height must be an integer")

    def test_for_valid_x_value(self):
        rec = Rectangle(12, 3, -2, 0, 7)
        self.assertRaises(ValueError, msg="x must be >= 0")

    def test_for_valid_y_value(self):
        rec = Rectangle(12, 3, 2, -4, 9)
        self.assertRaises(ValueError, msg="y must be >= 0")

    def test_for_valid_x_type(self):
        rec = Rectangle(12, 3, "two", 4, 8)
        self.assertRaises(TypeError, msg="x must be an integer")

    def test_for_valid_y_type(self):
        rec = Rectangle(12, 3, 2, "four", 8)
        self.assertRaises(TypeError, msg="y must be an integer")

    def test_area(self):
        rec = Rectangle(3, 2)
        self.assertEqual(rec.area(), 6)

    def test_str(self):
        rec = Rectangle(12, 7, 2, 1, 5)
        self.assertEqual(str(rec), "[Rectangle] (5) 2/1 - 12/7")
