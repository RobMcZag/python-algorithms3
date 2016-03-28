import unittest
import graph


class GraphTest(unittest.TestCase):

    __runSlowTests = False

    def testEmptyGraph(self):
        g = graph.Graph(5)
        self.assertIsNotNone(g)
        self.assertEqual(5, g._numvertices)
        self.assertEqual(0, g._numedges)

    def testAddEdge(self):
        g = graph.Graph(5)
        g.add_edge(1, 3)

        self.assertEqual(1, g._numedges)
        self.assertEqual(1, len(g.adjacents(1)))
        self.assertEqual(1, len(g.adjacents(3)))
        self.assertTrue(1 in g.adjacents(3))
        self.assertTrue(3 in g.adjacents(1))

    def testAddDoubleEdge(self):
        g = graph.Graph(5)
        g.add_edge(1, 3)
        g.add_edge(1, 3)

        self.assertEqual(2, g._numedges)
        self.assertEqual(2, len(g.adjacents(1)))
        self.assertEqual(2, len(g.adjacents(3)))
        self.assertTrue(1 in g.adjacents(3))
        self.assertTrue(3 in g.adjacents(1))

    def testAddSelfEdge(self):
        g = graph.Graph(5)
        g.add_edge(3, 3)

        self.assertEqual(1, g._numedges)
        self.assertEqual(2, len(g.adjacents(3)))    # 1 undirected edge can be traversed in 2 ways !
        self.assertTrue(3 in g.adjacents(3))

    def testSimpleGraph(self):
        g = graph.Graph(5)
        g.add_edge(1, 3)
        g.add_edge(2, 1)
        g.add_edge(3, 3)
        g.add_edge(4, 4)
        # print('simple graph :\n', g)

        self.assertEqual(4, g._numedges)
        self.assertEqual(0, len(g.adjacents(0)))
        self.assertEqual(2, len(g.adjacents(1)))
        self.assertEqual(3, len(g.adjacents(3)))    # Circular links counts x 2 vertexes !
        self.assertEqual(1, len(g.adjacents(2)))
        self.assertEqual(2, len(g.adjacents(4)))    # Circular links counts x 2 vertexes !
        self.assertTrue(1 in g.adjacents(3))
        self.assertTrue(1 in g.adjacents(2))
        self.assertTrue(3 in g.adjacents(1))
        self.assertTrue(3 in g.adjacents(3))
        self.assertTrue(4 in g.adjacents(4))

    def testToStringEmptyGraph(self):
        g = graph.Graph(5)
        sg = str(g)
        self.assertTrue("0 => []" in sg)

    def testToStringSimpleGraph(self):
        g = graph.Graph(5)
        g.add_edge(1, 3)
        g.add_edge(2, 1)
        g.add_edge(3, 3)
        g.add_edge(4, 4)
        # print('simple graph :\n', g)

        sg = str(g)
        self.assertTrue("0 => []" in sg)
        self.assertTrue("1 => [2, 3]" in sg or "1 => [3, 2]" in sg)
        self.assertTrue("2 => [1]" in sg)
        self.assertTrue("3 => [1, 3, 3]" in sg or "3 => [3, 3, 1]" in sg)
        self.assertTrue("4 => [4, 4]" in sg)

    def testLoadFromFileTiny(self):
        g = graph.Graph.from_file('tinyG.txt')
        # print(g)

        self.assertEqual(13, g.num_vertices())
        self.assertEqual(13, g.num_edges())
        self.assertTrue(0 in g.adjacents(5))
        self.assertTrue(3 in g.adjacents(5))
        self.assertTrue(5 in g.adjacents(3))

    def testLoadFromFileMedium(self):
        g = graph.Graph.from_file('mediumG.txt')
        # print(g)

        self.assertEqual(250, g.num_vertices())
        self.assertEqual(1273, g.num_edges())
        self.assertTrue(244 in g.adjacents(246))
        self.assertTrue(0 in g.adjacents(225))
        self.assertTrue(15 in g.adjacents(225))

    @unittest.skipUnless(__runSlowTests, "Skipping testLoadFromFileLarge as test is slow, takes about 15 seconds.\n")
    def testLoadFromFileLarge(self):
        g = graph.Graph.from_file('largeG.txt')
        self.assertEqual(1000000, g.num_vertices())
        self.assertEqual(7586063, g.num_edges())

    # Directed graphs
    def testLoadFromFileTinyDG(self):
        g = graph.Graph.from_file('tinyDG.txt', directed=True)
        # print('tinyDG.txt :\n', g)

        self.assertEqual(13, g.num_vertices())
        self.assertEqual(22, g.num_edges())
        self.assertTrue(1 in g.adjacents(0))
        self.assertFalse(2 in g.adjacents(0))
        self.assertTrue(6 in g.adjacents(8))
        self.assertTrue(8 in g.adjacents(6))

    def testLoadFromFileTinyDAG(self):
        g = graph.Graph.from_file('tinyDAG.txt', directed=True)
        # print('tinyDAG.txt :\n', g)

        self.assertEqual(13, g.num_vertices())
        self.assertEqual(15, g.num_edges())
        self.assertTrue(1 in g.adjacents(0))
        self.assertFalse(2 in g.adjacents(0))
        self.assertTrue(6 in g.adjacents(7))
        self.assertTrue(7 in g.adjacents(8))


if __name__ == '__main__':
    unittest.main()
