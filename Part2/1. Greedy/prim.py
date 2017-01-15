import heapq


def make_graph(edges):
    """Makes graph as adjacency map from a sequence of weighted edges"""
    def add_vertex(v, g):
        """Adds vertex v to graph g"""
        if not v in g:
            g[v] = dict()

    g = dict()
    for (head, tail, cost) in edges:
        add_vertex(head, g)
        add_vertex(tail, g)

        g[head][tail] = cost
        g[tail][head] = cost
        vertices_count = len(g)
        if vertices_count % 10000 == 0:
            print("Vertices added: %d" % vertices_count)

    return g

def prims_msp(graph):

    msp = list()

    explored = set()

    crossing_edges_map = {v : [float("inf"), v, v] for v in graph}

    crossing_edges_heap = list(crossing_edges_map.itervalues())

    while crossing_edges_heap:

        (cost, start, finish) = tuple(crossing_edges_heap.pop(0))

        if (not start == finish ):
            msp.append( (start, finish, cost) )

        explored.add(finish)

        for v, v_cost in graph[finish].iteritems():
            if crossing_edges_map[v][0] > v_cost:
                crossing_edges_map[v][0] = v_cost # update cost
                crossing_edges_map[v][1] = finish # update start

        heapq.heapify(crossing_edges_heap)

    return msp

def weight(edges):
    return sum(( cost for v,u,cost in edges ))





