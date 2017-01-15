import unittest
import scc

graph1 = {1: [2, 3], 2: [4], 3: [4], 4: []}
edges1 = [(1,2), (1,3), (2,4), (3,4)]

edges2 = [
    (1,2),
    (2,3), (2,4),
    (3,1),
    (4, 5),
    (5, 6), (5, 7),
    (6, 4),
    (7, 8),
    (8, 9),
    (9, 7)
    ]

class MakeGraphTestCase(unittest.TestCase):
    def test_make_graph_empty(self):
        self.assertEqual(dict(), scc.make_graph(list()), "make_graph failed")

    def test_make_graph1(self):
        self.assertEqual(graph1, scc.make_graph(edges1), "make_graph failed")

class DFSTestCase(unittest.TestCase):
    def test_dfs_graph1_v4(self):
        self.assertSequenceEqual(scc.dfs(scc.make_graph(edges1), 4)[0], [4])
    def test_dfs_graph1_v1(self):
        self.assertSetEqual(scc.dfs(scc.make_graph(edges1), 1)[0], [4, 2, 3, 1])
##    def test_dfs_graph1_v1_v2(self):
##        self.assertSequenceEqual(scc.dfs(graph1, 1, explored = [4, 3]), [4, 3, 2, 1])
##    def test_dfs_graph1_v1_v3(self):
##        self.assertSequenceEqual(gr, 1, marked = {4, 3}), [2, 1])

class SCCTestCase(unittest.TestCase):
    def test_dfs_edges1(self):
        self.assertEqual(len(scc.scc_e(edges1)), 4)
    def test_dfs_edges2(self):
       self.assertEqual(len(scc.scc_e(edges2)), 3)

if __name__ == '__main__':
    unittest.main()