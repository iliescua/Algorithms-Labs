from collections import deque, defaultdict
import copy
import sys

class Vertex:
    """
    Models vertices in a graph.  The pi, color, and d attributes
    are used to store information as part of a breadth-first search.
    The name attribute is used for a unique identifier for each
    vertex.
    """
    def __init__(self, pi=None, color="WHITE", d=sys.maxsize, name=None):
        self.pi = pi
        self.color = color
        self.d = d
        self.name = name

def load_data(training_flname, testing_flname):
    """
    Loads the training and testing set data. Returns
    a pair of graphs corresponding to the two data sets.
    """
    # We want to avoid creating duplicate Vertex objects
    # for the same user.  We will check the dictionary for
    # an existing Vertex object before creating another
    vertices = dict()
    with open(training_flname) as fl:
        G1 = DiGraph()
        for ln in fl:
            cols = ln.split()
            if cols[0] not in vertices:
                vertices[cols[0]] = Vertex(name=cols[0])
            if cols[1] not in vertices:
                vertices[cols[1]] = Vertex(name=cols[1])
            u = vertices[cols[0]]
            v = vertices[cols[1]]
            G1.add_edge(u, v)
            
    with open(testing_flname) as fl:
        G2 = DiGraph()
        for ln in fl:
            cols = ln.split()
            if cols[0] not in vertices:
                vertices[cols[0]] = Vertex(name=cols[0])
            if cols[1] not in vertices:
                vertices[cols[1]] = Vertex(name=cols[1])
            u = vertices[cols[0]]
            v = vertices[cols[1]]
            G2.add_edge(u, v)

    return G1, G2

def precision(recommendations, testing_set):
    """
    Precision measures the fraction of positive predictions
    were found in the test set (were true positives).

    A precise algorithm rarely makes false positive predictions.
    """
    rec_edges = recommendations.edge_set()
    test_edges = testing_set.edge_set()
    intersection = rec_edges.intersection(test_edges)
    
    if len(rec_edges) == 0:
        return 0.0
    
    return float(len(intersection)) / len(rec_edges)
    
def recall(recommendations, testing_set):
    """
    Recall measures the fraction of test set that
    were predicted positively.
    """
    rec_edges = recommendations.edge_set()
    test_edges = testing_set.edge_set()
    intersection = rec_edges.intersection(test_edges)
    
    if len(test_edges) == 0:
        return 0.0
    
    return float(len(intersection)) / len(test_edges)

def bfs(G, s):
    """
    Performs a breadth-first search of the graph G, starting at vertex s.
    """
    for ver in G._edges:
        ver.color = 'WHITE'
        ver.d = sys.maxsize
        ver.pi = None
    s.color = 'GRAY'
    s.d = 0
    s.pi = None
    que = deque([s])
    while(len(que) != 0):
        ver = que.popleft()
        for adjVer in G._edges[ver]:
            if(adjVer.color == 'WHITE'):
                adjVer.color = 'GRAY'
                adjVer.d = ver.d + 1
                adjVer.pi = ver
                que.append(adjVer)
        ver.color = 'BLACK'
        
def recommend_friends_for_user(G, s, max_depth):
    """
    Performs a breadth-first search of the graph G, starting at vertex s.
    Does not traverse vertices with d > max_depth.
    Returns a list of all vertices encountered.
    """
    for ver in G._edges:
        ver.color = 'WHITE'
        ver.d = sys.maxsize
        ver.pi = None
    s.color = 'GRAY'
    s.d = 0
    s.pi = None
    que = deque([s])
    traversed = []
    while(len(que) != 0):
        ver = que.popleft()
        for adjVer in G._edges[ver]:
            if(adjVer.color == 'WHITE'):
                adjVer.color = 'GRAY'
                adjVer.d = ver.d + 1
                adjVer.pi = ver
                if (adjVer.d <= max_depth):
                    que.append(adjVer)
                    traversed.append(adjVer)
                else: 
                    continue
        ver.color = 'BLACK'
    return traversed


def recommend_all_friends(G, max_depth):
    """
    Generates recommendations for all users by performing
    a depth-limited breadth-first search for each user.
    
    The resulting recommendations are stored as a DiGraph.
    """
    allFriends = DiGraph()
    for ver in G._edges:
        traversed = recommend_friends_for_user(G, ver, max_depth)
        for adjVer in traversed:
            allFriends.add_edge(ver, adjVer)
            allFriends.add_edge(adjVer, ver)
    return allFriends


class DiGraph:
    """
    Implements a directed graph.
    
    Vertices can be any hashable object (e.g., number, string, tuple).
    
    The graph is stored using a dictionary.  The vertices are keys.
    The value for each vertex is a set of vertices.  An edge from vertex
    u to vertex v is present in the graph if v in self._edges[u].
    """
    
    def __init__(self):
        self._edges = defaultdict(set)
        
    def add_vertex(self, v):
        """
        Adds the given vertex v. If v is already in the
        graph, it isn't added again.
        """
        self._edges[v]

    def add_edge(self, u, v):
        """
        Adds an edge from vertex u to vertex v.  If the edge is
        already in the graph, if it isn't added again.  If u or
        v are not present in the graph, they are added.
        """
        self._edges[v]
        self._edges[u]
        self._edges[u].add(v)

    def vertex_exists(self, u):
        """
        Returns true if u is in the graph, false otherwise.
        """
        return True if u in self._edges else False
    
    def edge_exists(self, u, v):
        """
        Returns true if there is an edge from u to v in the graph, false otherwise.
        If u or v are not in the graph, false is returned.
        """
        return True if v in self._edges[u] else False
   
    def get_outgoing_edges(self, u):
        """
        Returns a collection of edges starting at vertex u.
        """
        return self._edges[u]
    
    def count_vertices(self):
        """
        Counts the number of vertices in the graph
        """
        return len(self._edges)
        
    def count_edges(self):
        """
        Counts the number of edges in the graph
        """
        lst = map(len, self._edges.values())
        return sum(lst) 

    def edge_set(self):
        """
        Creates 2-tuple of adjacent verticies in an edge
        """
        cnt = 1
        while (cnt < self.count_edges):
            tup = (self._edges[cnt -1], self._edges[cnt])
            cnt += 1
        return tup
