import json
import os
import queue
import unittest

from JavaClass import JavaClass
from JavaMember import JavaMember
from parser import Parser


class TestIsComplexType(unittest.TestCase):
    def test_is_complex_type_string(self):
        parser = Parser()
        self.assertFalse(parser.is_complex_type("hello"))

    def test_is_complex_type_int(self):
        parser = Parser()
        self.assertFalse(parser.is_complex_type(5))

    def test_is_complex_type_float(self):
        parser = Parser()
        self.assertFalse(parser.is_complex_type(5.5))

    def test_is_complex_type_bool(self):
        parser = Parser()
        self.assertFalse(parser.is_complex_type(True))

    def test_is_complex_type_list(self):
        parser = Parser()
        self.assertTrue(parser.is_complex_type([]))

    def test_is_complex_type_dict(self):
        parser = Parser()
        self.assertTrue(parser.is_complex_type(dict()))


class TestBuildClass(unittest.TestCase):
    def test_build_class_flat_and_primitive(self):
        parser = Parser()

        expected_members = [
            JavaMember(
                access_specifier="private",
                variable_type="String",
                variable_name="playerInfo",
            ),
            JavaMember(
                access_specifier="private",
                variable_type="Integer",
                variable_name="ttl",
            ),
            JavaMember(
                access_specifier="private",
                variable_type="Boolean",
                variable_name="hasHuTao",
            ),
            JavaMember(
                access_specifier="private",
                variable_type="Double",
                variable_name="decimal",
            ),
        ]

        with open(os.path.join(os.getcwd(), "TestData", "BuildClass", "SimpleJson.json")) as f:
            test_data = f.read()

        test_data = json.loads(test_data)

        built_class = parser.build_class("userDetail", test_data)

        self.assertTrue(isinstance(built_class, JavaClass))
        self.assertEqual(built_class.class_name, "UserDetail")
        self.assertEqual(built_class.package_name, "com.example.enkaapi.models")
        self.assertListEqual(built_class.members, expected_members)

    def test_build_class_object(self):
        parser = Parser()

        expected_members = [
            JavaMember(
                access_specifier="private",
                variable_type="PlayerInfo",
                variable_name="playerInfo",
            ),
        ]

        with open(os.path.join(os.getcwd(), "TestData", "BuildClass", "SingleDictJson.json")) as f:
            test_data = f.read()

        test_data = json.loads(test_data)

        built_class = parser.build_class("userDetail", test_data)

        self.assertTrue(isinstance(built_class, JavaClass))
        self.assertEqual(built_class.class_name, "UserDetail")
        self.assertEqual(built_class.package_name, "com.example.enkaapi.models")
        self.assertListEqual(built_class.members, expected_members)

    def test_build_class_list(self):
        pass

    def test_build_class_map(self):
        pass

    def test_build_class_null(self):
        parser = Parser()

        test_data = '''
        {
            "playerInfo":null
        }
        '''

        test_data = json.loads(test_data)

        self.assertRaises(RuntimeError, parser.build_class, "userDetail", test_data)

class TestAddChildrenToQueue(unittest.TestCase):
    def test_add_children_to_queue_simple_types(self):
        parser = Parser()
        q = queue.Queue()
        with open(os.path.join(os.getcwd(), "TestData", "AddChildrenToQueue", "SimpleJson.json")) as f:
            test_data = f.read()

        test_data = json.loads(test_data)
        parser.add_children_to_queue(q, test_data)
        self.assertTrue(q.empty())

    def test_add_children_to_queue_dict_types(self):
        parser = Parser()
        q = queue.Queue()

        expected_values = [
            ("playerInfo", {}),
            ("numbers", {}),
        ]

        with open(os.path.join(os.getcwd(), "TestData", "AddChildrenToQueue","DictJson.json")) as f:
            test_data = f.read()

        test_data = json.loads(test_data)

        parser.add_children_to_queue(q, test_data)
        self.assertTupleEqual(expected_values[0], q.get())
        self.assertTupleEqual(expected_values[1], q.get())
        self.assertTrue(q.empty())
