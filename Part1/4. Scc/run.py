import scc
import collections

def main():
    # edges = list()
    # file = open("SCC.txt")
    # for line in file:
    #     l = line.split()
    #     edges.append((int(l[0]), int(l[1])))
    # file.close()
    #
    # graph = scc.make_graph(edges)
    #
    # file = open("SCC_al.txt", "w")
    # for (head, tails) in graph.items():
    #     file.write(str(head))
    #     file.write(" ")
    #     file.write(" ".join(str(v) for v in tails))
    #     file.write("\n")
    # file.close()
    #
    # graph_reversed = scc.make_graph((v, u) for (u, v) in edges)
    #
    # file = open("SCC_al_rev.txt", "w")
    # for (head, tails) in graph_reversed.items():
    #     file.write(str(head))
    #     file.write(" ")
    #     file.write(" ".join(str(v) for v in tails))
    #     file.write("\n")
    # file.close()

    graph = dict()
    file = open("SCC_al.txt")
    for line in file:
        l = line.split()
        v = int (l.pop(0))
        graph[v] = [ int(x) for x in l ]
    file.close()

    print("Graph loaded [%d vertices]" % len(graph))

    graph_reversed = dict()
    file = open("SCC_al_rev.txt")
    for line in file:
        l = line.split()
        v = int (l.pop(0))
        graph_reversed[v] = [ int(x) for x in l ]
    file.close()

    print("Reversed graph loaded [%d vertices]" % len(graph_reversed))

    final = scc.scc(graph, graph_reversed)

    print("Final: %s" % final)

if __name__ == '__main__':
    main()
