# <nbformat>2</nbformat>
# <markdowncell>
"""
Networks is a module that implements a network of nodes connected by
edges, and various algorithms and measurements implemented on networks.
(This type of data structure is also known in mathematics as a graph.
What we deal with specifically here are undirected graphs, where there is
no direction or asymmetry between the nodes that delineate an edge.)
This module contains the core code needed to define and manipulate
networks, independently of how they are created or what their context is.
We use the Networks module as part of other problem modules, such as
SmallWorld and Percolation.
"""

# <codecell>
# Import the necessary libraries.
import NetGraphics  # a separate module supporting network visualization
reload(NetGraphics) 

# <markdowncell>
# -----------------------------------------------------------------------
#
# Defining undirected graph class: used by both Small World and Percolation
# exercises.
#
# -----------------------------------------------------------------------

# <codecell>
class UndirectedGraph:
    """An UndirectedGraph g contains a dictionary (g.connections) that
    maps a node identifier (key) to a list of nodes connected to (values).
    g.connections[node] returns a list [node2, node3, node4] of neighbors.
    Node identifiers can be any non-mutable Python type (e.g., integers,
    tuples, strings, but not lists).
    """
    
    def __init__(self):
        """UndirectedGraph() creates an empty graph g.
	g.connections starts as an empty dictionary.  When nodes are
	added, the corresponding values need to be inserted into lists.

        A method/function definition in a class must begin with an instance
        of the class in question; by convention, the name "self" is used for
        this instance."""
        self.connections = {}

    def HasNode(self, node):
        """Returns True if the graph contains the specified node, and
        False otherwise.  Check directly to see if the dictionary of
        connections contains the node, rather than (inefficiently)
        generating a list of all nodes and then searching for the
        specified node."""
        return self.connections.has_key(node)

    def AddNode(self, node):
	"""Uses HasNode(node) to determine if node has already been added."""
        if not self.HasNode(node):
            self.connections[node] = []
    
    def AddEdge(self, node1, node2):
        """
	Add node1 and node2 to network first
	Adds new edge 
	(appends node2 to connections[node1] and vice-versa, since it's
	an undirected graph)
	Do so only if old edge does not already exist 
	(node2 not in connections[node1])
	"""
        self.AddNode(node1)
        self.AddNode(node2)
        if node2 not in self.connections[node1]:
            self.connections[node1].append(node2)
            self.connections[node2].append(node1)

    def GetNodes(self):
        """g.GetNodes() returns all nodes (keys) in connections"""
        return self.connections.keys()

    def GetNeighbors(self, node):
        """g.GetNeighbors(node) returns a copy of the list of neighbors of
        the specified node.  A copy is returned (using the [:] operator) so
		that the user does not inadvertently change the neighbor list."""
        if self.HasNode(node):
            return self.connections[node][:]
        return []

# <markdowncell>
# Simple test routines

# <codecell>
def pentagraph():
    """pentagraph() creates a simple 5-node UndirectedGraph, and then uses
    the imported NetGraphics module to layout and display the graph.
    The graph is returned from the function.
    """
    g = UndirectedGraph()
    g.AddEdge(0,2)
    g.AddEdge(0,3)
    g.AddEdge(1,3)
    g.AddEdge(1,4)
    g.AddEdge(2,4)
    NetGraphics.DisplayCircleGraph(g)
    return g

# <codecell>
def circle8():
    """circle8() creates an 8-node UndirectedGraph, where the nodes are
    arranged in a circle (ring), and then uses the imported NetGraphics
    module to layout and display the graph.  The graph is returned from
    the function.
    """
    g = UndirectedGraph()
    #g.AddEdge(0,1)
    #g.AddEdge(1,2)
    #g.AddEdge(2,3)
    #g.AddEdge(3,4)
    #g.AddEdge(4,5)
    #g.AddEdge(5,6)
    #g.AddEdge(6,7)
    #g.AddEdge(7,0)
    for x in range(0,8):
        for y in range(x,8):
            g.AddEdge(x,y)
    NetGraphics.DisplayCircleGraph(g)
    return g


# <markdowncell>
# ***** After building and testing your network class, build some    ***** #
# ***** Small World or Percolation networks, making use of the       ***** #
# ***** corresponding hints file. Then return to analyze these       ***** #
# ***** networks using the general-purpose routines you write below. ***** #

# <markdowncell>
# ***** Small World exercise routines start here                     ***** #

# <markdowncell>
# -----------------------------------------------------------------------
#
# Routines for finding path lengths on graphs: used by the Small World
# Network exercise only
#
# -----------------------------------------------------------------------

# <codecell>
def FindPathLengthsFromNode(graph, node):
    """Breadth--first search. See "Six degrees of separation" exercise
    from Sethna's book.  Use a dictionary to store the distance to
    each node visited.  Keys in the dictionary thus serve as markers
    of nodes that have already been visited, and should not be considered
    again."""
    path_lengths = {}
    path_lengths[node] = 0
    done = False
    while not done:
        done = True
        for next_node in path_lengths.keys():
            neighbors = graph.GetNeighbors(next_node)
            for neighbor in neighbors:
                if not neighbor in path_lengths:
                    path_lengths[neighbor] = path_lengths[next_node]+1
                    done = False
    return path_lengths

# <codecell>
def FindAllPathLengths(graph):
    """
    FindAllPathLengths returns a dictionary, indexed by node pairs
    in tuples, storing the shortest path length between those nodes,
    e.g. for small-world networks.
    """
    lengths = {}
    nodes = graph.GetNodes()
    for node1 in nodes:
        node1_lengths = FindPathLengthsFromNode(graph, node1)
        for node2 in node1_lengths.keys():
            lengths[(node1,node2)] = node1_lengths[node2]
    return lengths

# <codecell>
def FindAveragePathLength(graph):
    """Averages path length over all pairs of nodes"""
    lengths = FindAllPathLengths(graph)
    nodes1 = graph.GetNodes()
    nodes2 = graph.GetNodes()
    num_nodes = len(nodes1)
    num_edges = (num_nodes * (num_nodes-1))/2
    cum_length = 0
    for node1 in nodes1:
        nodes2.remove(node1)
        for node2 in nodes2:
            cum_length += lengths[(node1,node2)]
    avg_length = 1.0 * cum_length / num_edges
    return avg_length

# <markdowncell>
# -----------------------------------------------------------------------
#
# Routine for calculating the clustering coefficient of a graph.
# This was a piece of the original Small World paper, but is not part of the 
# assigned exercise.
#
# -----------------------------------------------------------------------

# <codecell>
def ComputeClusteringCoefficient(graph):
    """Computes clustering coefficient of graph"""
    pass

# <markdowncell>
# -----------------------------------------------------------------------
#
# Routines for calculating "betweenness", which measures how many shortest
# paths between pairs of nodes on a graph pass through a given node or edge.
# Used in the Small Worlds exercise.
#
# References: (on the Web site)
# Mark E. J. Newman, "Scientific collaboration networks. ii. shortest paths,
# weighted networks, and criticality", Physical Review E 64: 016132, 2002.
# Michelle Girvan and Mark E. J. Newman, "Community structure in social
# and biological networks. Proceedings of the National Academy of Sciences
# 12, 7821-7826, 2002.
#
# -----------------------------------------------------------------------

# <codecell>
def EdgeAndNodeBetweennessFromNode(graph, node):
    """
    Newman's edge and node betweenness inner loop
    Returns partial sum of edge, node betweenness
    """
    pass

# <codecell>
def EdgeAndNodeBetweenness(graph):
    """Returns Newman's edge, node betweenness"""
    pass

# <markdowncell>
# -----------------------------------------------------------------------
#
# Sample routines for reading in external files defining networks. Used
# primarily for the later portions of the Small World exercise.
#
# -----------------------------------------------------------------------

# <codecell>
def ReadGraphFromEdgeFile(filename, conversion=None):
    """Reads file with (node1,node2) for each edge in graph"""
    pass

# <codecell>
def ReadGraphFromNeighborFile(filename, conversion=None):
    """
    Reads file with [node1,node2,node3] for completely interconnected
    group of nodes (as in actors in a movie)
    Should be read in as a bipartite graph!
    """
    pass


# <markdowncell>
# ***** Percolation exercise routines start here                     ***** #
# -----------------------------------------------------------------------
#
# Routines for finding clusters in networks. Used in the Percolation exercise.
#
# -----------------------------------------------------------------------

# <codecell>
def ClusterCompare(c1, c2):
    if len(c2) < len(c1):
        return -1
    if len(c2) == len(c1):
        return 0

    return 1

# <codecell>
def FindClusterFromNode(graph, node, visited=None):
    """Breadth--first search
    The dictionary "visited" should be initialized to False for
    all the nodes in the cluster you wish to find
    It's used in two different ways.
    (1) It's passed back to the
        calling program with all the nodes in the current cluster set to
        visited[nodeInCluster]=True, so that the calling program can skip
        nodes in this cluster in searching for other clusters.
    (2) It's used internally in this algorithm to keep track of the
        sites in the cluster that have already been found and incorporated
    See "Building a Percolation Network" in text for algorithm"""
    visited[node] = True
    cluster = [node]
    currentShell = graph.GetNeighbors(node)

    while currentShell:
        nextShell = []
        for nextNode in currentShell:
            if not visited[nextNode]:
                cluster.append(nextNode)
                visited[nextNode] = True
                nextShell.extend(graph.GetNeighbors(nextNode))
        currentShell = nextShell[:]

    return cluster
                

# <codecell>
def FindAllClusters(graph):
    """For example, find percolation clusters
    Set up the dictionary "visited" for FindClusterFromNode
    Set up an empty list "clusters"
    Iterate over the nodes;
        if it haven't been visited,
            find the cluster containing it
            append it to the cluster list
        return clusters
    Check your answer using
    NetGraphics.DrawSquareNetworkBonds(g, cl) and
    NetGraphics.DrawSquareNetworkSites(g, cl)
					            
    Optional: You may wish to sort your list of clusters according to their
    lengths, biggest to smallest
    For a list ell, the built-in method ell.sort() will sort the list
    from smallest to biggest;
    ell.sort(cmp) will sort the list according to the comparison function
    cmp(x, y) returns -1 if x < y, returns 0 if x==y, and returns 1 if x>y
    Define ReverseLengthCompare to compare two lists according to the
    unusual definition of inequality, l1<l2 if # len(l1) > len(l2)!
    """
    # Initialize visited dictionary
    visited = {}
    for node in graph.GetNodes():
        visited[node] = False

    # Find the clusters
    clusters = []
    for node in graph.GetNodes():
        if not visited[node]:
            clusters.append(FindClusterFromNode(graph, node, visited))

    # Return the clusters
    clusters.sort(ClusterCompare)
    return clusters

# <codecell>
def GetSizeDistribution(clusters):
    """Given the clusters, makes up a dictionary giving the number
    of clusters of a given size.
    """
    sizeDistribution = {}
    for cluster in clusters:
        if not sizeDistribution.has_key(len(cluster)):
            sizeDistribution[len(cluster)] = 0
        sizeDistribution[len(cluster)] += 1

    return sizeDistribution

# <markdowncell>
# Copyright (C) Cornell University
# All rights reserved.
# Apache License, Version 2.0


