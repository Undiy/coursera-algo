import unittest
import twosum


class TwosumTestCase(unittest.TestCase):
    def test1(self):
        # assert(twosum.twosum_exists({1, 25, -1000, 1042}, 42))
        self.assertEqual(twosum.twosum_count({1, 25, -1000, 1042}, (42, 26, 500)), 2)
    def test2(self):
        # assert(not twosum.twosum_exists({1036, -2543, 23444, -23443}, 0))
        self.assertEqual(twosum.twosum_count({1036, -2543, 23444, -23443}, (1, -1507)), 2)
if __name__ == '__main__':
    unittest.main()