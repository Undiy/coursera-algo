import unittest
import median


class MedianTestCase(unittest.TestCase):
    def test1(self):
        self.assertEquals(median.median_list([1,2,3,4,5,6]), [1, 1, 2, 2, 3, 3])

    def test2(self):
        self.assertEquals(median.median_list([1,4,12,2,3,8]), [1, 1, 4, 2, 3, 3])

    def test3(self):
        self.assertEquals(median.median_list([100,25,38,39,16,101]), [100, 25, 38, 38, 38, 38])

if __name__ == '__main__':
    unittest.main()