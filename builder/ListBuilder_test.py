import json
import unittest

from JavaMember import JavaMember
from builder import ListBuilder


class ListBuilderTest(unittest.TestCase):
    def test_build_as_member(self):
        test_data = json.loads('[]')

        expected = JavaMember(variable_type="List<Test>", variable_name="testList")
        actual = ListBuilder("testList", test_data).build_as_member()
        self.assertEqual(expected, actual)
