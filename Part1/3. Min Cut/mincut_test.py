import unittest
import mincut

graph1 = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}

graph2 = {}
graph2[1] = [2, 5, 6]
graph2[2] = [1, 3, 5, 6]
graph2[3] = [2, 4, 7, 8]
graph2[4] = [3, 7, 8]
graph2[5] = [1, 2, 6]
graph2[6] = [1, 2, 5, 7]
graph2[7] = [3, 4, 6, 8]
graph2[8] = [3, 4, 7]

# class ContractTest(unittest.TestCase):
#    def test_graph1(self):
#        assert(2 <= mincut.contract(graph1, verbose = True) <= 3)
#
#    def test_graph2(self):
#        assert(2 <= mincut.contract(graph2, verbose = True) <= 24)

class MinCutTest(unittest.TestCase):
    def test_graph1(self):
        self.assertEqual(mincut.mincut(graph1, max = 2, seed = 0), 2)

    def test_graph2(self):
        self.assertEqual(mincut.mincut(graph2, max = 2, seed = 0), 2)

    def test_graph40(self):
        graph40 = dict()
        file = open("test_case.txt")
        for line in file:
            l = line.split()
            v = int (l.pop(0))
            graph40[v] = [ int(x) for x in l ]
        file.close()
        #80000
        self.assertEqual(mincut.mincut(graph40, max = 3, seed = 0, show_seed_rate=500), 3)

if __name__ == '__main__':
    unittest.main()
