import json
import os
import unittest

from JavaClass import JavaClass
from JavaMember import JavaMember
from builder import MapBuilder


class MapBuilderTest(unittest.TestCase):
    def test_build_as_member(self):
        test_data = json.loads('{}')

        expected = JavaMember(variable_type="Map<String, Test>", variable_name="testMap")
        actual = MapBuilder("testMap", test_data).build_as_member()
        self.assertEqual(expected, actual)

    def test_build_as_member_primitive(self):
        test_data = json.loads('''{
            "1": 10164.1064453125,
            "2": 4780,
            "3": 0.10490000247955322,
            "4": 930.9654541015625,
            "5": 398.5400085449219,
            "6": 0.9975999593734741,
            "7": 614.843505859375,
            "20": 0.6969000101089478,
            "21": 0,
            "22": 1.9464359283447266,
            "23": 1.4534000158309937
        }''')

        expected = JavaMember(variable_type="Map<String, Double>", variable_name="fightPropMap")
        actual = MapBuilder("fightPropMap", test_data).build_as_member()

        self.assertEqual(expected, actual)

    def test_build_members_map_optional_fields(self):
        with open(os.path.join(os.getcwd(), "TestData", "BuildMembers", "MapOptionalFields.json")) as f:
            test_data = json.loads(f.read())

        expected = [
            JavaMember(variable_type="Integer", variable_name="type"),
            JavaMember(variable_type="String", variable_name="ival"),
            JavaMember(variable_type="String", variable_name="val"),
        ]

        actual = MapBuilder("testMap", test_data).build_members()

        self.assertListEqual(expected, actual)

    def test_build_as_class_primitve(self):
        test_data = json.loads('''
        {
            "0": 1,
            "1": 1
        }
        ''')

        list_builder = MapBuilder("testDataList", test_data)

        self.assertRaises(
            RuntimeError,
            list_builder.build_as_class,
            "com.example.enkaapi.models")

    def test_build_as_class_map_optional_fields(self):
        with open(os.path.join(os.getcwd(), "TestData", "BuildMembers", "MapOptionalFields.json")) as f:
            test_data = json.loads(f.read())

        members = [
            JavaMember(variable_type="Integer", variable_name="type"),
            JavaMember(variable_type="String", variable_name="ival"),
            JavaMember(variable_type="String", variable_name="val"),
        ]

        expected_class = JavaClass(
            class_name="Test",
            package_name="com.example.enkaapi.models",
            members=members
        )

        actual_class = MapBuilder("testMap", test_data).build_as_class("com.example.enkaapi.models")

        self.assertEqual(expected_class, actual_class)
