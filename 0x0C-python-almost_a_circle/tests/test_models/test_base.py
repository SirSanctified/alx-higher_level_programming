import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_is_None(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_is_not_None(self):
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
