"""
Undirected graph data type and procedures for its manipulation.
"""

from collections import deque
import sys


class Graph:
    """
    Generic purpose data structure to represent an directed or undirected graph in a time and memory efficient way.\n
    Vertexes are named with consecutive numbers starting from 0
    (the last is V-1, being V the number of vertexes in the graph).

    **Implementation notes**:
    This implementation is based on an adjacency-list representation of the graph:
    for every vertex V we maintain a list of adjacent vertexes,
    i.e. vertexes reachable from V with a direct connection (an edge).
    """

    def __init__(self, numvertices, directed=False):
        """Creates a graph with the given number of vertices and no edges.

        :param directed: True if the graph is a directed graph; default is False, i.e. an undirected graph.
        :return: an empty graph with a structure to hold edges for the given number of vertexes
        :rtype: Graph
        """
        self._numvertices = numvertices
        self._directed = directed
        self._numedges = 0
        self._adjacents = [list() for _ in range(0, numvertices)]

    @classmethod
    def from_file(cls, filename: str, directed = False):
        """Loads a graph definition from a file.

        First line must contain the number of vertexes;
        second line must contain the number of edges;
        from third line onward there must be two integers representing the two vertexes to be connected by and edge.

        :param filename: the name of the file containing the graph definition.
        :param directed: True if the graph is a directed graph; default is False, i.e. an undirected graph.
        :return: a graph built from the information stored in the file
        :rtype: Graph
        """
        with open(filename) as fh:
            vertnum = int(fh.readline().strip())
            int(fh.readline().strip())
            graph = Graph(vertnum, directed)

            for line in fh:
                numstr = line.split()
                v1 = int(numstr[0])
                v2 = int(numstr[1])
                graph.add_edge(v1, v2)

        return graph

    def is_directed(self):
        """:return: True if the graph is a directed graph, False if is an undirected graph."""
        return self._directed

    def num_vertices(self) -> int:
        """:return: the number of vertices of this Graph."""
        return self._numvertices

    def num_edges(self) -> int:
        """:return: the number of edges of this Graph."""
        return self._numedges

    def add_edge(self, vertex1, vertex2):
        """
        Add and edge connecting vertex1 to vertex2.
        An edge is not added if it is already present.

        :param vertex1: the first vertex of the edge being added.
        :param vertex2: the second vertex of the edge being added.
        :return: None
        """
        self._numedges += 1
        self._adjacents[vertex1].append(vertex2)
        if not self._directed:
            self._adjacents[vertex2].append(vertex1)

    def adjacents(self, vertex):
        return self._adjacents[vertex]

    def __str__(self):
        lines = []
        for v, adjacents in enumerate(self._adjacents):
            if len(adjacents) > 0:
                adjstr = str(adjacents)
            else:
                adjstr = "[]"
            lines.append(str(v) + " => " + adjstr + "\n")
        return "".join(lines)


class DepthFirstSearch:
    """
    Finds the vertexes connected with the given source vertex and a path (not necessarily the shortest) to reach it.
    """
    def __init__(self, graph: Graph, source_vertex: int):
        """Navigate the given Graph from the given source vertex using Depth First Search.

        :param graph: the graph we want to navigate.
        :param source_vertex: the vertex where we start the navigation.
        :return: a DepthFirstSearch object to query the graph starting from the given source vertex.
        """
        self._source = source_vertex
        self._visited = [False] * graph.num_vertices()
        self._predecessor = [-1] * graph.num_vertices()

        self._predecessor[source_vertex] = source_vertex
        self._count = self._depth_first_search(graph, source_vertex)

    def _depth_first_search(self, graph: Graph, vertex: int):
        count = 0
        self._visited[vertex] = True

        for v in graph.adjacents(vertex):
            if not self._visited[v]:
                self._predecessor[v] = vertex
                count += self._depth_first_search(graph, v)

        return count + 1

    def connected(self, vertex: int):
        """
        :param vertex: the vertex we want to know if it is connected to the source fro the current Graph.
        :return: True if the given vertex is connected to the source, False otherwise.
        """
        return self._visited[vertex]

    def count(self) -> int:
        """:return: How many vertexes are connected with the source, including the source in the count."""
        return self._count

    def path_to(self, vertex: int):
        """Find a path from the given vertex to the source.

        :param vertex: the vertex to find a path to the source
        :return: a list with the vertexes to navigate to get to the source if it is connected or None otherwise
        """
        path = None
        if self.connected(vertex):
            path = []
            while vertex != self._source:
                path.append(vertex)
                vertex = self._predecessor[vertex]
            path.append(self._source)

        return path


class BreadthFirstSearch:
    """
    Finds the vertexes connected with the given source vertex and a the shortest path to reach each.
    """
    def __init__(self, graph: Graph, source_vertex: int):
        """Navigate the given Graph from the given source vertex using Breadth First Search.

        :param graph: the graph we want to navigate.
        :param source_vertex: the vertex where we start the navigation.
        :return: a BreadthFirstSearch object to query the graph starting from the given source vertex.
        """
        self._graph = graph
        self._source = source_vertex
        self._queue = deque()
        self._visited = [False] * self._graph.num_vertices()
        self._predecessor = [-1] * self._graph.num_vertices()
        self._distance = [sys.maxsize] * self._graph.num_vertices()
        self._count = 0
        self._breadth_first_search(self._source)

    def _breadth_first_search(self, source):
        self._visited[source] = True
        self._predecessor[source] = source
        self._distance[source] = 0
        self._queue.append(source)
        while len(self._queue) > 0:
            v = self._queue.popleft()
            self._count += 1
            for adj in self._graph.adjacents(v):
                if not self._visited[adj]:
                    self._visited[adj] = True
                    self._predecessor[adj] = v
                    self._distance[adj] = self._distance[v] + 1
                    self._queue.append(adj)

    def connected(self, vertex: int):
        """
        :param vertex: the vertex we want to know if it is connected to the source fro the current Graph.
        :return: True if the given vertex is connected to the source, False otherwise.
        """
        return self._visited[vertex]

    def count(self) -> int:
        """:return: How many vertexes are connected with the source, including the source in the count."""
        return self._count

    def path_to(self, vertex: int):
        """Find a path from the given vertex to the source.

        :param vertex: the vertex to find a path to the source
        :return: a list with the vertexes to navigate to get to the source if it is connected or None otherwise
        """
        path = None
        if self.connected(vertex):
            path = []
            while vertex != self._source:
                path.append(vertex)
                vertex = self._predecessor[vertex]
            path.append(self._source)

        return path

    def distance(self, vertex: int):
        """
        :param vertex: the vertex we want to know if it is connected to the source fro the current Graph.
        :return: the distance between the given vertex and the source.
        """
        return self._distance[vertex]


class ConnectedComponents:
    """Determines the connected components in an undirected graph."""

    def __init__(self, graph: Graph):
        """ Analyzes the given graph and store the results to be ready to answer for queries on connected components.

        :param graph: The Graph to analyze
        """
        self._visited = [False] * graph.num_vertices()
        self._group = [-1] * graph.num_vertices()
        self._group_size = [-1] * graph.num_vertices()
        self._count = 0

        for v in range(graph.num_vertices()):
            if not self._visited[v]:
                self._visited[v] = True
                self._group[v] = v
                self._count += 1
                print("Checking CC for vertex ", v)
                dfs = DepthFirstSearch(graph, v)
                self._group_size[v] = dfs.count()
                for w in range(v+1, graph.num_vertices()):
                    if dfs.connected(w):
                        self._visited[w] = True
                        self._group[w] = v
                        self._group_size[w] = dfs.count()

    def count(self):
        """:return: The number of different connected components. """
        return self._count

    def connected(self, v: int, w: int) -> bool:
        """ :return: True if the two vertexes are connected, False otherwise."""
        return self._group[v] == self._group[w]

    def group(self, vertex: int) -> int:
        """:return: The id of the connected component the given vertex is part of."""
        return self._group[vertex]

    def groupsize(self, vertex: int) -> int:
        """:return: The size of the connected component the given vertex is part of."""
        return self._group_size[vertex]


class CycleDetector:
    """A class to detect cycles in undirected graphs.
    Cycles can be self loops, parallel edges or multi vertec circular paths.
    """
    pass


"""
More depth-first search applications.

    Cycle detection: Is a given graph acyclic? Cycle.java uses depth-first search to determine whether a graph has a
    cycle, and if so return one. It takes time proportional to V + E in the worst case.

    Two-colorability:
    Can the vertices of a given graph be assigned one of two colors in such a way that no edge
    connects vertices of the same color?
    Bipartite.java uses depth-first search to determine whether a graph has a bipartition;
    if so, return one; if not, return an odd-length cycle. It takes time proportional to V + E in the worst case.

    Bridge:
    A bridge (or cut-edge) is an edge whose deletion increases the number of connected components.
    Equivalently, an edge is a bridge if and only if it is not contained in any cycle.
    Bridge.java uses depth-first search to find time the bridges in a graph.
    It takes time proportional to V + E in the worst case.

    Biconnectivity:
    An articulation vertex (or cut vertex) is a vertex whose removal increases the number of connected components.
    A graph is biconnected if it has no articulation vertices. Biconnected.java uses depth-first search to find
    the bridges and articulation vertices. It takes time proportional to V + E in the worst case.

    Planarity:
    A graph is planar if it can be drawn in the plane such that no edges cross one another.
    The Hopcroft-Tarjan algorithm is an advanced application of depth-first search that determines whether a graph
    is planar in linear time.
"""
