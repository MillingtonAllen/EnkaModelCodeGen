import json
import os.path
import unittest

from JavaClass import JavaClass
from JavaMember import JavaMember
from builder import ListBuilder


class ListBuilderTest(unittest.TestCase):
    def test_build_as_member(self):
        test_data = json.loads('[]')

        expected = JavaMember(variable_type="List<Test>", variable_name="testList")
        actual = ListBuilder("testList", test_data).build_as_member()
        self.assertEqual(expected, actual)

    def test_build_as_member_primitive(self):
        test_data = json.loads('''[
            210101,
            210017,
            210016,
            210003,
            210082,
            210004,
            210059,
            210069,
            210045
        ]''')

        expected = JavaMember(variable_type="List<Integer>", variable_name="showNameCardIdList")
        actual = ListBuilder("showNameCardIdList", test_data).build_as_member()

        self.assertEqual(expected, actual)

    def test_build_members_list_optional_fields(self):
        with open(os.path.join(os.getcwd(), "TestData", "BuildMembers", "ListOptionalFields.json")) as f:
            test_data = json.loads(f.read())

        expected = [
            JavaMember(variable_type="Integer", variable_name="avatarId"),
            JavaMember(variable_type="Integer", variable_name="level"),
            JavaMember(variable_type="Integer", variable_name="costumeId"),
        ]

        actual = ListBuilder("testData", test_data).build_members()

        self.assertListEqual(expected, actual)

    def test_build_as_class_primitve(self):
        test_data = json.loads("[1, 2, 3]")

        list_builder = ListBuilder("testDataList", test_data)

        self.assertRaises(
            RuntimeError,
            list_builder.build_as_class,
            "com.example.enkaapi.models")

    def test_build_as_class(self):
        with open(os.path.join(os.getcwd(), "TestData", "BuildMembers", "ListOptionalFields.json")) as f:
            test_data = json.loads(f.read())

        members = [
            JavaMember(variable_type="Integer", variable_name="avatarId"),
            JavaMember(variable_type="Integer", variable_name="level"),
            JavaMember(variable_type="Integer", variable_name="costumeId"),
        ]

        expected_class = JavaClass(
            class_name="TestData",
            package_name="com.example.enkaapi.models",
            members=members
        )

        actual_class = ListBuilder("testDataList", test_data).build_as_class("com.example.enkaapi.models")

        self.assertEqual(expected_class, actual_class)


