import unittest

from builder import TypedBuilderFactory, PrimitiveBuilder, MapBuilder, ListBuilder, ObjectBuilder


class TypedBuilderFactoryTest(unittest.TestCase):
    def test_create_primitive_str(self):
        actual = TypedBuilderFactory.create("test", "Hello")
        self.assertIsInstance(actual, PrimitiveBuilder)

    def test_create_primitive_int(self):
        actual = TypedBuilderFactory.create("test", 5)
        self.assertIsInstance(actual, PrimitiveBuilder)

    def test_create_primitive_bool(self):
        actual = TypedBuilderFactory.create("test", True)
        self.assertIsInstance(actual, PrimitiveBuilder)

    def test_create_primitive_float(self):
        actual = TypedBuilderFactory.create("test", 3.5)
        self.assertIsInstance(actual, PrimitiveBuilder)

    def test_create_map(self):
        actual = TypedBuilderFactory.create("testMap", {})
        self.assertIsInstance(actual, MapBuilder)

    def test_create_list(self):
        actual = TypedBuilderFactory.create("testList", [])
        self.assertIsInstance(actual, ListBuilder)

    def test_create_dict(self):
        actual = TypedBuilderFactory.create("test", {})
        self.assertIsInstance(actual, ObjectBuilder)