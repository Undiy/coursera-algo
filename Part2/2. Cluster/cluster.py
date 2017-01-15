import unoinfind

def max_cluster_spacing(nodes, edges, target_cluster_count):

    edges.sort()

    clusters = unoinfind.UnionFind()

    clusters.insert_objects(nodes)

    for cost, v, u in edges:
        if (clusters.find(v) != clusters.find(u)):

            if (len(clusters.num_weights) <= target_cluster_count):
                print clusters
                return cost
            else:
                clusters.union(v, u)
                # print clusters

def load(file):
    edges = list()
    nodes = set()
    file = open(file)
    for line in file:
        l = line.split()
        if len(l) > 2:
            edges.append( (int(l[2]), int(l[0]), int(l[1])) )
            nodes.add(edges[-1][1])
            nodes.add(edges[-1][2])
    file.close()

    return nodes, edges






