import unittest
import graph


class BreadthFirstSearchTest(unittest.TestCase):

    __runSlowTests = False

    def testTinyGraph(self):
        g = graph.Graph.from_file('tinyG.txt')
        bfs = graph.BreadthFirstSearch(g, 0)

        self.assertEqual(7, bfs.count())

        self.assertFalse(bfs.connected(7))
        self.assertIsNone(bfs.path_to(7))
        self.assertFalse(bfs.connected(8))
        self.assertIsNone(bfs.path_to(8))
        self.assertFalse(bfs.connected(9))
        self.assertIsNone(bfs.path_to(9))
        self.assertFalse(bfs.connected(12))
        self.assertIsNone(bfs.path_to(12))

        self.assertEqual([2, 0], bfs.path_to(2))
        self.assertEqual(1, bfs.distance(2))

        self.assertEqual([3, 5, 0], bfs.path_to(3))
        self.assertEqual(2, bfs.distance(3))

        self.assertEqual([4, 5, 0], bfs.path_to(4))
        self.assertEqual(2, bfs.distance(4))

        self.assertEqual([5, 0], bfs.path_to(5))
        self.assertEqual(1, bfs.distance(5))

    def testMedGraph(self):
        g = graph.Graph.from_file('mediumG.txt')
        bfs = graph.BreadthFirstSearch(g, 0)

        self.assertEqual(250, bfs.count())
        self.assertTrue(bfs.connected(123))
        self.assertEqual(9, bfs.distance(123))
        self.assertEqual([123, 246, 8, 210, 139, 92, 171, 165, 68, 0], bfs.path_to(123))


"""
        dfs = graph.DepthFirstSearch(g, 7)
        self.assertEqual([8,7], dfs.path_to(8))

        dfs = graph.DepthFirstSearch(g, 10)
        self.assertEqual([12, 11, 9, 10], dfs.path_to(12))
"""

if __name__ == '__main__':
    unittest.main()
