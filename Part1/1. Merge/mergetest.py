import unittest

import mergesort
import unittest

a1 = [3, 1, 2]
a2 = [1, 3, 2, 42]

class SortTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(mergesort.mergesort(a1), sorted(a1))

    def test_11(self):
        self.assertEqual(mergesort.mergesort([1, 2, 3]), [1, 2, 3])

    def test_12(self):
        self.assertEqual(mergesort.mergesort([1, 3, 2, 42]), [1, 2, 3, 42])

    def test_12(self):
        '''1, 3, 2, 5, 4, 7, 6, 42 -> 1, 2, 3, 4, 5, 6, 7, 42'''
        self.assertEqual(mergesort.mergesort([1, 3, 2, 5, 4, 7, 6, 42]), [1, 2, 3, 4, 5, 6, 7, 42])

    def test_2(self):
        '''23, 17, 25, 100, 2, 24 -> 2, 17, 23, 24, 25, 100'''
        self.assertEqual(mergesort.mergesort([23, 17, 25, 100, 2, 24]), [2, 17, 23, 24, 25, 100])

    def test_21(self):
        '''23, 17, 25, 100, 2, 24 -> 2, 17, 23, 24, 25, 100'''
        self.assertEqual(mergesort.mergesort([2, 17, 23, 24, 25, 100]), [2, 17, 23, 24, 25, 100])

class CountTest(unittest.TestCase):
    def test_3(self):
        '''3, 1, 2 -> 3 inversions'''
        self.assertEqual(mergesort.mergesortcount([3, 1, 2])[1], 2)

    def test_31(self):
        '''1, 2, 3 -> 0 inversions'''
        self.assertEqual(mergesort.mergesortcount([1, 2, 3])[1], 0)

    def test_32(self):
        '''1, 3, 5, 2, 4, 6 -> 3 inversions'''
        self.assertEqual(mergesort.mergesortcount([1, 3, 5, 2, 4, 6])[1], 3)

    def test_33(self):
        '''1, 3, 5, 2, 4, 6 -> 3 inversions'''
        self.assertEqual(mergesort.mergesortcount([6, 5, 4, 3, 2, 1])[1], 15)

    def test_33(self):
        '''1, 3, 5, 2, 4, 6 -> 3 inversions'''
        self.assertEqual(mergesort.mergesortcount([1000, 1, 2, 3, 4, 5])[1], 5)




if __name__ == '__main__':
    unittest.main()
