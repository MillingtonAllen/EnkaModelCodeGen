import json
import os.path
import unittest

from JavaClass import JavaClass
from JavaMember import JavaMember
from builder import ObjectBuilder


class ObjectBuilderTest(unittest.TestCase):
    def test_build_as_member(self):
        test_data = json.loads('{}')

        expected = JavaMember(variable_type="Test", variable_name="test")
        actual = ObjectBuilder("test", test_data).build_as_member()
        self.assertEqual(expected, actual)

    def test_build_members(self):
        test_file_location = os.path.join(os.getcwd(), "TestData", "BuildMembers", "BuildMembers.json")
        with open(test_file_location) as f:
            test_data = json.loads(f.read())

        expected_members = [
            JavaMember(access_specifier="private", variable_type="PlayerInfo", variable_name="playerInfo"),
            JavaMember(access_specifier="private", variable_type="Map<String, Artifacts>",
                       variable_name="artifactsMap"),
            JavaMember(access_specifier="private", variable_type="List<AvatarInfo>", variable_name="avatarInfoList"),
            JavaMember(access_specifier="private", variable_type="Integer", variable_name="ttl"),
            JavaMember(access_specifier="private", variable_type="String", variable_name="uid"),
            JavaMember(access_specifier="private", variable_type="Boolean", variable_name="hasHuTao"),
            JavaMember(access_specifier="private", variable_type="Double", variable_name="energyRecharge"),
        ]
        actual_members = ObjectBuilder("testData", test_data).build_members()

        self.assertListEqual(expected_members, actual_members)

    def test_build_as_class(self):
        test_file_location = os.path.join(os.getcwd(), "TestData", "BuildMembers", "BuildMembers.json")
        with open(test_file_location) as f:
            test_data = json.loads(f.read())

        members = [
            JavaMember(access_specifier="private", variable_type="PlayerInfo", variable_name="playerInfo"),
            JavaMember(access_specifier="private", variable_type="Map<String, Artifacts>",
                       variable_name="artifactsMap"),
            JavaMember(access_specifier="private", variable_type="List<AvatarInfo>", variable_name="avatarInfoList"),
            JavaMember(access_specifier="private", variable_type="Integer", variable_name="ttl"),
            JavaMember(access_specifier="private", variable_type="String", variable_name="uid"),
            JavaMember(access_specifier="private", variable_type="Boolean", variable_name="hasHuTao"),
            JavaMember(access_specifier="private", variable_type="Double", variable_name="energyRecharge"),
        ]

        expected_class = JavaClass(
            class_name="TestData",
            package_name="com.example.enkaapi.models",
            members=members
        )

        actual_class = ObjectBuilder("testData", test_data).build_as_class("com.example.enkaapi.models")

        self.assertEqual(expected_class, actual_class)
