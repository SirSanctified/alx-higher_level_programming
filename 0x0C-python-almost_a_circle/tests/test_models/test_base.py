import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_is_None(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_is_not_None(self):
        b2 = Base(12)
        self.assertEqual(b2.id, 12)

    def test_to_json_string(self):
        b2 = Base()
        self.assertIn(
                b2.to_json_string(
                    [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
                    ),
                '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
                )
        self.assertEqual(b2.to_json_string([]), '[]')
