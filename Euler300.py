###############################################################################
# Euler 300 - Protein Folding
# Kelvin Blaser     2015.2.6
#
# The solution structure is as follows:
#   Make all folding patterns
#   Turn folding pattern into graph
#   Remove sub-graphs
#   Calculate max-H-H points for each protein pattern
#
# Solution: 65979 / 8192 = 8.0540771484375  
###############################################################################
from fractions import Fraction

def makeFoldPatterns(N):
    '''
    Recursively generate the ways a protein can fold.  Each fold is represented
    by a list of positions in x-y space.  We remove some redundancy by only
    considering folds with start with (0,0),(0,1).
    '''
    patterns = []
    
    def updateFoldPattern(pattern):
        if len(pattern) == N:
            patterns.append(pattern)
            return
            
        x,y = pattern[-1]
        next_spot = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        for n in next_spot:
            if n in pattern:
                continue
            updateFoldPattern(pattern+[n])
        return

    updateFoldPattern([(0,0),(0,1)])
    return patterns

def pattern2graph(pattern):
    '''
    Change the pattern, which a list of positions, to a graph of which
    components are connected to which.  The latter is a frozenset.

    Placing the graphs in a set will remove some more redundancy.
    '''
    graph = []
    for n in range(len(pattern)):
        x,y = pattern[n]
        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        for m in range(n+1,len(pattern)):
            if pattern[m] in neighbors:
                graph.append((n,m))
    return frozenset(graph)

def removeSubGraphs(graphs):
    '''
    Graphs is a set of frozensets.  Each frozenset is a graph of which protein
    components are connected.  If graph A is a subset of graph B, then there is
    no way graph A can have more H-H connections than graph B, so we can remove
    it from consideration.
    '''
    new_graphs = set()
    while len(graphs) > 0:
        g1 = graphs.pop()
        keep = True
        to_remove = []
        for g2 in graphs:
            if g2.issubset(g1):
                to_remove.append(g2)
            elif g1.issubset(g2):
                keep = False
                break
        for g2 in to_remove:
            graphs.discard(g2)
        if keep:
            new_graphs.add(g1)
    return new_graphs

def optimalFoldConnections(fold,N,graphs):
    '''
    The first N bits of the integer fold deterimine the H-P pattern.  For
    example, if N=4 and fold is 12 = 1100 base 2, the corresponding pattern is
    HHPP.
    For each graph in graphs, count the number of HH connections and return the
    maximum.
    '''
    if fold%1000 == 0:
        print '%i/%i Complete'%(fold, 2**N)
    
    component_pattern = [True]*N
    for x in range(N):
        if fold % 2:
            component_pattern[x] = False
        fold /= 2

    max_connections = 0
    for g in graphs:
        connection_count = 0
        for connection in g:
            n1,n2 = connection
            if component_pattern[n1] and component_pattern[n2]:
                connection_count += 1
        if connection_count > max_connections:
            max_connections = connection_count
    return max_connections

def Euler300(N):
    patterns = makeFoldPatterns(N)
    graphs = set(pattern2graph(p) for p in patterns)
    graphs = removeSubGraphs(graphs)
    
    connections = sum( optimalFoldConnections(fold,N,graphs)
                       for fold in range(2**N) )

    print Fraction(connections,2**N)
    print connections / 2.**N
    return Fraction(connections,2**N)
        
