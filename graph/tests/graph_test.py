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
        # print(g)

    def testToStringEmptyGraph(self):
        g = graph.Graph(5)
        sg = str(g)
        self.assertTrue("0 => {}" in sg)

    def testToStringSimpleGraph(self):
        g = graph.Graph(5)
        g.add_edge(1, 3)
        g.add_edge(2, 1)
        g.add_edge(3, 3)
        g.add_edge(4, 4)

        # print(g)
        sg = str(g)
        self.assertTrue("0 => {}" in sg)
        self.assertTrue("1 => {2, 3}" in sg or "1 => {3, 2}" in sg)
        self.assertTrue("2 => {1}" in sg)
        self.assertTrue("3 => {1, 3}" in sg or "3 => {3, 1}" in sg)
        self.assertTrue("4 => {4}" in sg)

    def testLoadFromFileTiny(self):
        g = graph.Graph.from_file('tinyG.txt')
        self.assertEqual(13, g.num_vertices())
        self.assertEqual(13, g.num_edges())
        self.assertTrue(0 in g.adjacents(5))
        self.assertTrue(3 in g.adjacents(5))
        self.assertTrue(5 in g.adjacents(3))
        # print(g)

    def testLoadFromFileMedium(self):
        g = graph.Graph.from_file('mediumG.txt')
        self.assertEqual(250, g.num_vertices())
        self.assertEqual(1273, g.num_edges())
        self.assertTrue(244 in g.adjacents(246))
        self.assertTrue(0 in g.adjacents(225))
        self.assertTrue(15 in g.adjacents(225))
        # print(g)

    @unittest.skipUnless(__runSlowTests, "Skipping testLoadFromFileLarge as test is slow, takes about 15 seconds.")
    def testLoadFromFileLarge(self):
        g = graph.Graph.from_file('largeG.txt')
        self.assertEqual(1000000, g.num_vertices())
        self.assertEqual(7586063, g.num_edges())

if __name__ == '__main__':
    unittest.main()
