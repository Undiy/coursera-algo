import unittest
import floyd_warshall


class ClusterTestCase(unittest.TestCase):
    def test1(self):
        n, m, edges = floyd_warshall.load_edges("test1.txt")
        graph = floyd_warshall.make_graph(edges)
        A = floyd_warshall.apsp(graph)
        print(A)
        self.assertEqual(floyd_warshall.min_path(A), -8)

    def test2(self):
        n, m, edges = floyd_warshall.load_edges("test2.txt")
        graph = floyd_warshall.make_graph(edges)
        A = floyd_warshall.apsp(graph)
        self.assertEqual(A, None)


if __name__ == '__main__':
    unittest.main()