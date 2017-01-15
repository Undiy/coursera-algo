import scc

def load_implication_graph(file):

    graph = dict()
    n = 0

    for line in open(file):
        l = line.split()
        if len(l) > 1:
            x = int(l[0])
            y = int(l[1])
            if not -x in graph:
                graph[-x] = set()
            if not -y in graph:
                graph[-y] = set()

            graph[-x].add(y)
            graph[-y].add(x)
        else:
            n = int(l[0])


    return graph

def load_implication_edges(file):

    edges = list()
    n = 0

    for line in open(file):
        l = line.split()
        if len(l) > 1:
            x = int(l[0])
            y = int(l[1])

            edges.append((-x, y))
            edges.append((-y, x))

        else:
            n = int(l[0])

    return edges


def reversed_graph(graph):

    graph_rev = dict()

    for v, s in graph.iteritems():
        for u in s:
            if not u in graph_rev:
                graph_rev[u] = set()
            graph_rev[u].add(v)

    return graph_rev

def is_solvable(edges):

    for scc_list in scc.scc_e(edges):
        for v in scc_list:
            if -v in scc_list:

                print"%d and %d in %s" % (v, -v, scc_list)

                return False

    return True


