import unittest
import graph


class GraphTest(unittest.TestCase):

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

        self.assertEqual(1, g._numedges)
        self.assertEqual(1, len(g.adjacents(1)))
        self.assertEqual(1, len(g.adjacents(3)))
        self.assertTrue(1 in g.adjacents(3))
        self.assertTrue(3 in g.adjacents(1))

    def testAddSelfEdge(self):
        g = graph.Graph(5)
        g.add_edge(3, 3)

        self.assertEqual(1, g._numedges)
        self.assertEqual(1, len(g.adjacents(3)))
        self.assertTrue(3 in g.adjacents(3))

    def testSimpleGraph(self):
        g = graph.Graph(5)
        g.add_edge(1, 3)
        g.add_edge(2, 1)
        g.add_edge(3, 3)
        g.add_edge(4, 4)

        self.assertEqual(4, g._numedges)
        self.assertEqual(0, len(g.adjacents(0)))
        self.assertEqual(2, len(g.adjacents(1)))
        self.assertEqual(2, len(g.adjacents(3)))
        self.assertEqual(1, len(g.adjacents(2)))
        self.assertEqual(1, len(g.adjacents(4)))
        self.assertTrue(1 in g.adjacents(3))
        self.assertTrue(1 in g.adjacents(2))
        self.assertTrue(3 in g.adjacents(1))
        self.assertTrue(3 in g.adjacents(3))
        self.assertTrue(4 in g.adjacents(4))
        #print(g)


if __name__ == '__main__':
    unittest.main()
