import unittest

from JavaMember import JavaMember
from builder import PrimitiveBuilder


class PrimitiveBuilderTest(unittest.TestCase):
    def test_build_as_member_str(self):
        expected = JavaMember(variable_type="String", variable_name="test")
        actual = PrimitiveBuilder("test", "Hello").build_as_member()
        self.assertEqual(expected, actual)

    def test_build_as_member_int(self):
        expected = JavaMember(variable_type="Integer", variable_name="test")
        actual = PrimitiveBuilder("test", 5).build_as_member()
        self.assertEqual(expected, actual)

    def test_build_as_member_bool(self):
        expected = JavaMember(variable_type="Boolean", variable_name="test")
        actual = PrimitiveBuilder("test", True).build_as_member()
        self.assertEqual(expected, actual)

    def test_build_as_member_float(self):
        expected = JavaMember(variable_type="Double", variable_name="test")
        actual = PrimitiveBuilder("test", 3.5).build_as_member()
        self.assertEqual(expected, actual)
