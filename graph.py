from random import randint

class Graph:
    """
    Graph data structure.
    """

    def __init__(self, fname = None, numVertices = None, numEdges = None, weightRange = None, directed = True):
        """
        Generates a weighted graph.
        """
        self.adjacent = {}
        self.weight = {}
        if fname == None:
            if any(arg == None for arg in (numVertices, numEdges, weightRange)):
                numVertices, numEdges, weightRange = map(int, input("numVertices, numEdges, weightRange: ").split())

            self.randomGraph(numVertices, numEdges, weightRange, directed)

        else:
            self.loadGraph(fname, directed)


    def numVertices(self):
        """
        Returns the number of vertices in the graph.
        """
        return len(self.adjacent)


    def vertices(self):
        """
        Returns the list of vertices in the graph.
        """
        return range(self.numVertices())


    def edges(self):
        """
        Returns a generator containing the edges in the graph.
        """
        return ((fromVertex,toVertex) for fromVertex in self.vertices() for toVertex in self.adjacent[fromVertex])


    def addDirectedEdge(self, fromVertex, toVertex, weight):
        """
        Inserts a weighted directed edge into the graph.
        """
        self.adjacent.setdefault(fromVertex, set()).add(toVertex)
        self.weight[(fromVertex, toVertex)] = weight


    def addUndirectedEdge(self, fromVertex, toVertex, weight):
        """
        Inserts a weighted undirected edge into the graph.
        """
        self.addDirectedEdge(fromVertex, toVertex, weight)
        self.addDirectedEdge(toVertex, fromVertex, weight)


    def randomGraph(self, numVertices, numEdges, weightRange, directed):
        """
        Generates a random graph.
        """
        addEdge = self.addDirectedEdge if directed else self.addUndirectedEdge

        for vertex in range(numVertices):
            self.adjacent[vertex] = set()

        for edge in range(numEdges):
            fromVertex = toVertex = None
            while fromVertex == toVertex:
                fromVertex = randint(0, numVertices-1)
                toVertex   = randint(0, numVertices-1)

            weight = randint(0, weightRange)
            addEdge(fromVertex, toVertex, weight)


    def loadGraph(fname, directed):
        """
        Loads a graph from a file containing a list of edges
        of the form: fromVertex, toVertex, weight.
        """ 
        addEdge = self.addDirectedEdge if directed else self.addUndirectedEdge
        with open(fname, 'r') as f:
            for vertex in range(int(f.readline())):
                self.adjacent[vertex] = set()

            for line in f.readlines():
                fromVertex, toVertex, weight = map(int, line.split())
                addEdge(fromVertex, toVertex, weight)


    def adjacentStr(self, fromVertex):
        """
        Returns a string representing the neighborhood of the
        given vertex.
        """
        return ", ".join(f"({toVertex}, {self.weight[(fromVertex, toVertex)]})" for toVertex in self.adjacent[fromVertex])


    def __str__(self):
        """
        Returns a string representing the graph.
        """
        return "\n".join(f"{vertex}: {self.adjacentStr(vertex)}" for vertex in range(self.numVertices()))


    def __repr__(self):
        """
        Represents the graph.
        """
        return str(self)

