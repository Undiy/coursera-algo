def load_edges(file):

    edges = list()
    n = 0
    m = 0

    for line in open(file):
        l = line.split()
        if len(l) > 2:
            edges.append( (l[0], l[1], int(l[2])) )
        else:
            n = int(l[0])
            m = int(l[1])

    return n, m, edges

def make_graph(edges):

    def add_vertex(graph, vertex):
        if not vertex in graph:
            graph[vertex] = dict()

    graph = dict()

    for tail, head, cost in edges:
        add_vertex(graph, tail)
        add_vertex(graph, head)
        graph[tail][head] = cost

    return graph

def apsp(graph):

    A = dict()

    coutndown = len(graph)

    for i in graph:
        A[i] = dict()
        for j in graph:
            if i == j:
                A[i][j] = 0
            elif j in graph[i]:
                A[i][j] = graph[i][j]
            else:
                A[i][j] = float('+inf')

    for k in graph:

        print('Vertex %s processing... (%d to do)' % (k, coutndown))
        coutndown -= 1

        A_new = dict()

        for i in graph:
            A_new[i] = dict()
            for j in graph:
                A_new[i][j] = min( A[i][j], A[i][k] + A[k][j] )
                if (i == j) and A_new[i][j] < 0:
                    print("Negative cycle detected!")
                    return None

        A = A_new

        # for v in graph:
        #     if A[v][v] < 0:
        #         return None

    return A

def min_path(A):
    if not A:
        return float('+inf')
    else:
        return min( (A[i][j], i, j) for i in A for j in A[i] )[0]