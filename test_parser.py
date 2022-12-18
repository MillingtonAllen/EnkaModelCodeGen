import json
import os
import queue
import unittest

from parser import Parser


class TestAddChildrenToQueue(unittest.TestCase):
    def test_add_children_to_queue_simple_types(self):
        parser = Parser()
        q = queue.Queue()
        with open(os.path.join(os.getcwd(), "TestData", "AddChildrenToQueue", "SimpleJson.json")) as f:
            test_data = f.read()

        test_data = json.loads(test_data)
        parser.add_children_to_queue(q, tuple(), "userDetail", test_data)
        self.assertTrue(q.empty())

    def test_add_children_to_queue_dict_types(self):
        parser = Parser()
        q = queue.Queue()

        expected_values = [
            (("playerInfo",), "playerInfo", {}),
            (("numbers",), "numbers", {}),
        ]

        with open(os.path.join(os.getcwd(), "TestData", "AddChildrenToQueue", "DictJson.json")) as f:
            test_data = f.read()

        test_data = json.loads(test_data)

        parser.add_children_to_queue(q, tuple(), "userDetail", test_data)
        self.assertTupleEqual(expected_values[0], q.get())
        self.assertTupleEqual(expected_values[1], q.get())
        self.assertTrue(q.empty())
