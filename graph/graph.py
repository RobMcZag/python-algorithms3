"""
Undirected graph data type and methods for its manipulation.
"""


class Graph:
    """
    Generic purpose data structure to represent an undirected graph in a time and memory efficient way.\n
    Vertexes are named with consecutive numbers starting from 0
    (the last is V-1, being V the number of vertexes in the graph).

    **Implementation notes**:
    This implementation is based on an adjacency-list representation of the graph:
    for every vertex V we maintain a list of adjacent vertexes,
    i.e. vertexes reachable from V with a direct connection (an edge).
    """

    def __init__(self, numvertices):
        self._numvertices = numvertices
        self._numedges = 0
        self._adjacents = [set() for x in range(0,numvertices)]

    @classmethod
    def from_file(cls, filename):
        """Loads a graph definition from a file.

        First line must contain the number of vertexes;
        second line must contain the number of edges;
        from third line onward there must be two integers representing the two vertexes to be connected by and edge.

        :param filename: the name of the file containing the graph definition.
        :type filename: str
        :return: a graph built from the information stored in the file
        :rtype: Graph
        """
        with open(filename) as fh:
            vertnum = int(fh.readline().strip())
            edgenum = int(fh.readline().strip())
            graph = Graph(vertnum)

            for line in fh:
                numstr = line.split()
                v1 = int(numstr[0])
                v2 = int(numstr[1])
                graph.add_edge(v1, v2)

        return graph

    def num_vertices(self):
        """
        :return: the number of vertices of this Graph.
        :rtype: int
        """
        return self._numvertices

    def num_edges(self):
        """
        :return: the number of edges of this Graph.
        :rtype: int
        """
        return self._numedges

    def add_edge(self, vertex1, vertex2):
        """
        Add and edge connecting vertex1 to vertex2.
        An edge is not added if it is already present.

        :param vertex1: the first vertex of the edge being added.
        :param vertex2: the second vertex of the edge being added.
        :return: None
        """
        if vertex1 not in self._adjacents[vertex2]:
            self._numedges += 1
            self._adjacents[vertex1].add(vertex2)
            self._adjacents[vertex2].add(vertex1)

    def adjacents(self, vertex):
        return self._adjacents[vertex]

    def __str__(self):
        lines = []
        for v, adjacents in enumerate(self._adjacents):
            if len(adjacents) > 0:
                adjstr = str(adjacents)
            else:
                adjstr = "{}"
            lines.append(str(v) + " => " + adjstr + "\n")
        return "".join(lines)
