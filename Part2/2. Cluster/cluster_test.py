import unittest
import cluster


class ClusterTestCase(unittest.TestCase):
    def test1(self):
        nodes, edges = cluster.load("test134365.txt")
        k = 4
        self.assertEquals(cluster.max_cluster_spacing(nodes, edges, k), 134365)

    def test2(self):
        nodes, edges = cluster.load("test2.txt")
        self.assertEquals(cluster.max_cluster_spacing(nodes, edges, 4), 2)
        self.assertEquals(cluster.max_cluster_spacing(nodes, edges, 3), 3)

    def test3(self):
        nodes, edges = cluster.load("test3.txt")
        self.assertEquals(cluster.max_cluster_spacing(nodes, edges, 4), 5)
        self.assertEquals(cluster.max_cluster_spacing(nodes, edges, 3), 6)

    def test4(self):
        nodes, edges = cluster.load("test4.txt")
        self.assertEquals(cluster.max_cluster_spacing(nodes, edges, 4), 27)
        self.assertEquals(cluster.max_cluster_spacing(nodes, edges, 3), 28)

    def test5(self):
        nodes, edges = cluster.load("test5.txt")
        self.assertEquals(cluster.max_cluster_spacing(nodes, edges, 4), 5)


if __name__ == '__main__':
    unittest.main()