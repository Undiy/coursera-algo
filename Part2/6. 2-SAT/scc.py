import copy

def make_graph(edges):
    """Makes graph as adjacency list from a sequence of edges"""
    def add_vertex(v, g):
        """Adds vertex v to graph g"""
        if not v in g:
            g[v] = list()

    g = dict()
    for (head, tail) in edges:
        add_vertex(head, g)
        add_vertex(tail, g)

        g[head].append(tail)
        vertices_count = len(g)
        # if vertices_count % 10000 == 0:
        #     print("Vertices added: %d" % vertices_count)

    return g

def dfs_rec(graph, source, explored = None, marked = None):
    """
    Depth-first search algoritm from the source vertex;
    returns explored verticies in reversed "topological" sequence
    """
    if explored is None:
        explored = list()  #collections.deque() # accumulates explored vertices
    if marked is None:
        marked = set() # vertices to be excluded from search

    if not (source in explored) and not (source in marked):
        marked.add(source)
        for v in graph[source]:
            explored = dfs(graph, v, explored, marked)

        explored.append(source)
    return explored

def dfs(graph, source):

##    g = copy.copy(graph)

    stack = [source]

    explored = list()

    marked = set()

    while stack:
        v = stack.pop()
        marked.add(v)

        if not v in graph:
            continue

        tails = [t for t in graph[v] if not t in marked]
        if tails:
            stack.append(v)
            stack.extend(tails)
        else:
            explored.append(v)
            del graph[v]

    return (explored, graph)

def scc_e(edges):

    graph = make_graph(edges)
    print("Graph constructed [%d vertices]" % len(graph))

    graph_reversed = make_graph((v, u) for (u, v) in edges)
    print("Reversed graph constructed [%d vertices]" % len(graph_reversed))

    return scc(graph, graph_reversed)

def scc(graph, graph_reversed):
    """
    Returns strong connected components of
    the graph represented by a sequence of edges
    as a list of sequences of nodes for each SCC
    """

    magic_sequence = list()

    vertices = list(graph_reversed.keys())

    for v in vertices:
        if v in graph_reversed:
            explored, graph_reversed = dfs(graph_reversed, v)
            magic_sequence.extend(explored)
        # if v % 500 == 0:
            # print("Processed: %d vertices | Remining: %d vertices" % (v, len(graph_reversed)))

    scc_list = list()


    magic_sequence.reverse()

##    file = open("magic_sequence.txt", "w")
##    for n in magic_sequence:
##        file.write("%d\n" % n)
##    file.close()

    print("Magic sequence reversed")

    for v in magic_sequence:
        if v in graph:
            scc, graph = dfs(graph, v)
            scc_list.append(scc)
            # print("SCC #%d: %s" % (len(scc_list), scc))

    # scc_lens = [len(scc) for scc in scc_list]
    # scc_lens.sort()

    return scc_list # scc_lens[-10:]





