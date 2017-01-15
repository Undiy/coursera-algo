import unittest
import shortest

graph1 = {
    "a": [("b", 1), ("c", 4)],
    "b": [("c", 2), ("d", 6)],
    "c": [("d", 3)],
    "d": []
}

sp1_a = {"a": 0, "b": 1, "c": 3, "d": 6}

graph2 = {
    "a": [("b", 1), ("c", 4), ("d", 6)],
    "b": [("c", 2), ("e", 8)],
    "c": [("d", 1), ("e", 3), ("f", 7)],
    "d": [("f", 11)],
    "e": [("g", 1)],
    "f": [("g", 5)],
    "g": []
}

sp2_a= {"a": 0, "b": 1, "c": 3, "d": 4, "e": 6, "f": 10, "g": 7}


class ShortestPathTestCase(unittest.TestCase):
    def test_graph1_a(self):
        self.assertEqual(shortest.shortest_path(graph1, "a"), sp1_a)
    def test_graph2_a(self):
        self.assertEqual(shortest.shortest_path(graph2, "a"), sp2_a)

if __name__ == '__main__':
    unittest.main()