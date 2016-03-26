import unittest
import graph


class ConnectedComponentsTest(unittest.TestCase):

    __runSlowTests = False

    def testTinyGraph(self):
        g = graph.Graph.from_file('tinyG.txt')
        cc = graph.ConnectedComponents(g)

        self.assertEqual(3, cc.count())
        print("Groups      are:", cc._group)
        print("Group sizes are:", cc._group_size)

        # Connected component n. 1
        self.assertTrue(cc.connected(0, 0))
        self.assertTrue(cc.connected(0, 1))
        self.assertTrue(cc.connected(0, 6))
        self.assertEqual(cc.group(0), cc.group(1))
        self.assertEqual(cc.group(0), cc.group(3))
        self.assertEqual(cc.group(0), cc.group(6))

        # Connected component n. 2
        self.assertFalse(cc.connected(0, 7))
        self.assertFalse(cc.connected(0, 8))
        self.assertTrue(cc.connected(7, 8))
        self.assertEqual(cc.group(7), cc.group(8))

        # Connected component n. 3
        self.assertFalse(cc.connected(0, 9))
        self.assertFalse(cc.connected(0, 12))
        self.assertTrue(cc.connected(9, 12))
        self.assertEqual(cc.group(9), cc.group(10))
        self.assertEqual(cc.group(9), cc.group(12))

    def testMediumGraph(self):
        g = graph.Graph.from_file('mediumG.txt')
        cc = graph.ConnectedComponents(g)

        self.assertEqual(1, cc.count())
        self.assertEqual(250, cc.groupsize(0))
        self.assertEqual(250, cc.groupsize(249))

        print("Groups      are:", cc._group)
        print("Group sizes are:", cc._group_size)


if __name__ == '__main__':
    unittest.main()
