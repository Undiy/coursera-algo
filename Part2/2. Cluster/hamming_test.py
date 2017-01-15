import hamming
import unittest

class ClusterTestCase(unittest.TestCase):
    def test1(self):
        nodes, radix = hamming.load("htest1.txt")
        self.assertEquals(hamming.count_hamming_clusters(nodes, radix, 3), 1)
    def test2(self):
        nodes, radix = hamming.load("htest2.txt")
        self.assertEquals(hamming.count_hamming_clusters(nodes, radix, 3), 3)



if __name__ == '__main__':
    unittest.main()