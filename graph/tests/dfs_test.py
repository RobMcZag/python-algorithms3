import unittest
import graph


class DepthFirstSearchTest(unittest.TestCase):

    __runSlowTests = False

    def setUp(self):
        self.g6 = graph.Graph(6)
        self.g6.add_edge(1, 2)
        self.g6.add_edge(1, 3)
        self.g6.add_edge(2, 3)
        self.g6.add_edge(2, 5)
        self.g6.add_edge(3, 4)
        self.g6.add_edge(4, 5)
        self.g6.add_edge(0, 0)

    def testCreate(self):
        dfs = graph.DepthFirstSearch(self.g6, 1)
        self.assertEqual(5, dfs.count())
        self.assertTrue(dfs.connected(5))
        self.assertTrue(dfs.connected(4))
        self.assertTrue(dfs.connected(3))
        self.assertTrue(dfs.connected(2))
        self.assertTrue(dfs.connected(1))
        self.assertFalse(dfs.connected(0))
        # print("visited = ", dfs._visited)
        # print("predecessor = ", dfs._predecessor)

    def testPathTo(self):
        dfs = graph.DepthFirstSearch(self.g6, 1)
        self.assertEqual([5, 4, 3, 2, 1], dfs.path_to(5))
        self.assertEqual([4, 3, 2, 1], dfs.path_to(4))
        self.assertEqual([3, 2, 1], dfs.path_to(3))
        self.assertEqual([2, 1], dfs.path_to(2))
        self.assertEqual([1], dfs.path_to(1))
        self.assertIsNone(dfs.path_to(0))
        # print("Path to 5: ", dfs.path_to(5))

    def testPathTo2(self):
        dfs = graph.DepthFirstSearch(self.g6, 3)
        self.assertIsNone(dfs.path_to(0))
        self.assertEqual([5, 2, 1, 3], dfs.path_to(5))
        self.assertEqual([4, 5, 2, 1, 3], dfs.path_to(4))
        self.assertEqual([3], dfs.path_to(3))
        self.assertEqual([2, 1, 3], dfs.path_to(2))
        self.assertEqual([1, 3], dfs.path_to(1))
        # print("Path to 5: ", dfs.path_to(5))

if __name__ == '__main__':
    unittest.main()
