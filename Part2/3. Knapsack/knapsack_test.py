import unittest
import knapsack


class ClusterTestCase(unittest.TestCase):
    def test1(self):
        size, things = knapsack.load("knapsack_test1.txt")
        self.assertEquals(knapsack.max_value(size, things), 60)

    def test2(self):
        size, things = knapsack.load("knapsack_test2.txt")
        self.assertEquals(knapsack.max_value(size, things), 27000)

    def test3(self):
        size, things = knapsack.load("knapsack_test3.txt")
        self.assertEquals(knapsack.max_value(size, things), 9)

    # def test_big_100(self):
    #     size, things = knapsack.load("knapsack_big.txt")
    #     self.assertEquals(knapsack.max_value(size, things[:100]), 1015873)

    def test_big_200(self):
        size, things = knapsack.load("knapsack_big.txt")
        self.assertEquals(knapsack.max_value(size, things[:200]), 1225054)




if __name__ == '__main__':
    unittest.main()