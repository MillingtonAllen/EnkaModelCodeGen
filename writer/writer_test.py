import os.path
import unittest

from JavaClass import JavaClass
from JavaMember import JavaMember
from writer import Writer

class WriterTest(unittest.TestCase):
    def test_write_empty_members(self):
        test_data = JavaClass(
            class_name="Output",
            package_name="TestData.writer",
            members=[]
        )

        with open(os.path.join(os.getcwd(),"TestData", "writer", "Output.java")) as f:
            expected = f.read()

        actual = Writer(test_data).write()

        self.assertEqual(expected, actual)

    def test_write_with_members(self):
        test_data = JavaClass(
            class_name="OutputWithMembers",
            package_name="TestData.writer",
            members=[
                JavaMember(
                    access_specifier="private",
                    variable_type="PlayerInfo",
                    variable_name="playerInfo"
                ),
                JavaMember(
                    access_specifier="private",
                    variable_type="List<AvatarInfo>",
                    variable_name="avatarInfoList"
                ),
                JavaMember(
                    access_specifier="private",
                    variable_type="Integer",
                    variable_name="ttl"
                ),
                JavaMember(
                    access_specifier="private",
                    variable_type="String",
                    variable_name="uid"
                ),
            ]
        )

        with open(os.path.join(os.getcwd(),"TestData", "writer", "OutputWithMembers.java")) as f:
            expected = f.read()

        actual = Writer(test_data).write()

        self.assertEqual(expected, actual)