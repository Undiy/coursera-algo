import unittest
import tsp

# class CrossingTestCase(unittest.TestCase):
    # def test1(self):
    #     points = tsp.load_points("tsp_test1.txt")
    #     graph, crossing = tsp.make_graph(points)
    #     tsp.massaged_graph(graph, crossing)
    #
    # def test2(self):
    #     points = tsp.load_points("tsp_test2.txt")
    #     graph = tsp.make_graph(points)
    #     print graph


class TSPTestCase(unittest.TestCase):
    def test1(self):
        points = tsp.load_points("tsp_test1.txt")
        graph = tsp.make_graph(points)
        self.assertEquals(tsp.tsp(graph), 4)

    def test2(self):
        points = tsp.load_points("tsp_test2.txt")
        graph = tsp.make_graph(points)

        self.assertEquals(round(tsp.tsp(graph), 4), 10.4721)

    def test3(self):
        points = tsp.load_points("tsp_test3.txt")
        graph = tsp.make_graph(points)
        self.assertEquals(round(tsp.tsp(graph), 5), 6.17986)

    def test4(self):
        points = tsp.load_points("tsp_test4.txt")
        graph = tsp.make_graph(points)
        self.assertEquals(round(tsp.tsp(graph), 5), 6.26533)

    def test5(self):
        points = tsp.load_points("tsp_test5.txt")
        graph = tsp.make_graph(points)
        self.assertEquals(round(tsp.tsp(graph), 3), 124.966)

    def test6(self):
        points = tsp.load_points("tsp_test6.txt")
        graph = tsp.make_graph(points)
        self.assertEquals(round(tsp.tsp(graph), 1), 16898.1)

    def test7(self):
        points = tsp.load_points("tsp_test7.txt")
        graph = tsp.make_graph(points)
        self.assertEquals(round(tsp.tsp(graph), 1), 26714.9)

    # def test1(self):
    #     points = tsp.load_points("tsp_test1.txt")
    #     self.assertEquals(tsp.min_route(points)[0], 4)
    #
    # def test2(self):
    #     points = tsp.load_points("tsp_test2.txt")
    #     self.assertEquals(round(tsp.min_route(points)[0], 4), 10.4721)

    # def test3(self):
    #     points = tsp.load_points("tsp_test3.txt")
    #     self.assertEquals(round(tsp.min_route(points)[0], 5), 6.17986)
    #
    # def test4(self):
    #     points = tsp.load_points("tsp_test4.txt")
    #     self.assertEquals(round(tsp.min_route(points)[0], 5), 6.26533)
    #
    # def test5(self):
    #     points = tsp.load_points("tsp_test5.txt")
    #     self.assertEquals(round(tsp.min_route(points)[0], 3), 124.966)
    #
    # def test6(self):
    #     points = tsp.load_points("tsp_test6.txt")
    #     self.assertEquals(round(tsp.min_route(points)[0], 1), 16898.1)

    # def test7(self):
    #     points = tsp.load_points("tsp_test7.txt")
    #     self.assertEquals(round(tsp.min_route(points)[0], 1), 26714.9)


if __name__ == '__main__':
    unittest.main()