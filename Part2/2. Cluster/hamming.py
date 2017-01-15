import unoinfind
import itertools

def load(file):
    nodes = set()
    file = open(file)
    for line in file:
        l = line.split()
        if len(l) > 2:
            nodes.add(int("".join(l), 2))
        elif len(l) == 2:
            radix = int(l[1])
    file.close()

    # print len(nodes)
    # print radix

    return nodes, radix

def neighbors(node, distance, radix):

    def invert_bits(node, bits):
        for bit in bits:
            node = node ^ 1 << bit
        return node

    return set(invert_bits(node, bits) for bits in itertools.combinations(xrange(0, radix), distance))

    # if distance == 1:
    #     return set(node ^ 1 << x for x in xrange(0, radix))
    #
    # if distance == 2:
    #     return set((node ^ 1 << x) ^ 1 << y for x in xrange(0, radix) for y in xrange(x, radix))

def count_hamming_clusters(nodes, radix, distance):

    clusters = unoinfind.UnionFind()
    clusters.insert_objects(nodes)

    for d in (1, 2):
        for node in nodes:
            for n1 in neighbors(node, d, radix).intersection(nodes):
                if clusters.find(node) != clusters.find(n1):
                    clusters.union(node, n1)
            # print("Node %d done for distance %d" % (node, d))

    # print clusters
    return len(clusters.num_weights)