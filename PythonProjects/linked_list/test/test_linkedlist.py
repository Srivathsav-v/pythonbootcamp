import unittest
from src.linkedlist import LinkedList
from src.linkedlist import Node


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.node = Node(10)
        self.linkedlist = LinkedList()

    def test_insertAtHead(self):
        pass


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
