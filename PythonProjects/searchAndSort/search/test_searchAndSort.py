import unittest
from searchAndSort import Search

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Search(nums=list(range(1,100)))

        self.s2 = Search(nums=['a', 'b', 'c'])

    def test_valid_target(self):
        target = 10
        self.assertEqual(self.s.binary_search(target), True)

    def test_invalid_target(self):
        target = 10000
        self.assertEqual(self.s.binary_search(target), False)

    def test_invalid_nums(self):
        target = 10
        self.assertEqual(self.s2.binary_search(target), TypeError)



if __name__ == '__main__':
    unittest.main()
