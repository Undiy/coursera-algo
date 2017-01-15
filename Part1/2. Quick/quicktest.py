import random
import quicksort
import unittest

a1 = [3, 1, 2]
a2 = [1, 3, 2, 42]
a3 = [180, 917, 699, 316, 47, 94, 226, 695, 284, 458, 458]

n = 42

class SortTest(unittest.TestCase):
    def test_1_1(self):
        a1_to_sort = a1[:]
        self.assertEqual(3, quicksort.qiucksort(a1_to_sort, 1))
        self.assertEqual(a1_to_sort, sorted(a1))


    def test_2_2(self):
        a2_to_sort = a2[:]
        self.assertEqual(5, quicksort.qiucksort(a2_to_sort, 1))
        self.assertEqual(a2_to_sort, sorted(a2))

    def test_1_2(self):
        a1_to_sort = a1[:]
        self.assertEqual(2, quicksort.qiucksort(a1_to_sort, 2))
        self.assertEqual(a1_to_sort, sorted(a1))


    def test_2_2(self):
        a2_to_sort = a2[:]
        self.assertEqual(5, quicksort.qiucksort(a2_to_sort, 2))
        self.assertEqual(a2_to_sort, sorted(a2))

##    def test_random_p1(self):
##        rand_arr = [random.randint(0,1000) for r in range(n)]
##        print("p1: %s" % rand_arr)
##        rand_arr_old = rand_arr[:]
##        quicksort.qiucksort(rand_arr, 1)
##        self.assertEqual(rand_arr, sorted(rand_arr_old))
##
##    def test_random_p2(self):
##        rand_arr = [random.randint(0,1000) for r in range(n)]
##        print("p2: %s" % rand_arr)
##        rand_arr_old = rand_arr[:]
##        quicksort.qiucksort(rand_arr, 2)
##        self.assertEqual(rand_arr, sorted(rand_arr_old))

    def test_random_p0(self):
        rand_arr = [random.randint(0,1000) for r in range(n)]
        rand_arr.append(rand_arr[-1])
        print("p0: %s" % rand_arr)
        rand_arr_old = rand_arr[:]
        quicksort.qiucksort(rand_arr)
        self.assertEqual(rand_arr, sorted(rand_arr_old))

    def test_3(self):
        a3_to_sort = a3[:]
        quicksort.qiucksort(a3_to_sort)
        self.assertEqual(a3_to_sort, sorted(a3))
##    def test_11(self):
##        self.assertEqual(mergesort.mergesort([1, 2, 3]), [1, 2, 3])
##
##    def test_12(self):
##        self.assertEqual(mergesort.mergesort([1, 3, 2, 42]), [1, 2, 3, 42])
##
##    def test_12(self):
##        '''1, 3, 2, 5, 4, 7, 6, 42 -> 1, 2, 3, 4, 5, 6, 7, 42'''
##        self.assertEqual(mergesort.mergesort([1, 3, 2, 5, 4, 7, 6, 42]), [1, 2, 3, 4, 5, 6, 7, 42])
##
##    def test_2(self):
##        '''23, 17, 25, 100, 2, 24 -> 2, 17, 23, 24, 25, 100'''
##        self.assertEqual(mergesort.mergesort([23, 17, 25, 100, 2, 24]), [2, 17, 23, 24, 25, 100])
##
##    def test_21(self):
##        '''23, 17, 25, 100, 2, 24 -> 2, 17, 23, 24, 25, 100'''
##        self.assertEqual(mergesort.mergesort([2, 17, 23, 24, 25, 100]), [2, 17, 23, 24, 25, 100])
##
##class CountTest(unittest.TestCase):
##    def test_3(self):
##        '''3, 1, 2 -> 3 inversions'''
##        self.assertEqual(mergesort.mergesortcount([3, 1, 2])[1], 2)
##
##    def test_31(self):
##        '''1, 2, 3 -> 0 inversions'''
##        self.assertEqual(mergesort.mergesortcount([1, 2, 3])[1], 0)
##
##    def test_32(self):
##        '''1, 3, 5, 2, 4, 6 -> 3 inversions'''
##        self.assertEqual(mergesort.mergesortcount([1, 3, 5, 2, 4, 6])[1], 3)
##
##    def test_33(self):
##        '''1, 3, 5, 2, 4, 6 -> 3 inversions'''
##        self.assertEqual(mergesort.mergesortcount([6, 5, 4, 3, 2, 1])[1], 15)
##
##    def test_33(self):
##        '''1, 3, 5, 2, 4, 6 -> 3 inversions'''
##        self.assertEqual(mergesort.mergesortcount([1000, 1, 2, 3, 4, 5])[1], 5)




if __name__ == '__main__':
    unittest.main()
