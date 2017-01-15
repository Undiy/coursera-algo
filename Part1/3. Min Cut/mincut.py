import random
from copy import deepcopy

def contract(graph, verbose = False, seed = None):
    "Contract a graph to a 2-vertex graphs"

    def rename_vertex(adj_list, v_super, v_merged):
        return [v_super if (v == v_merged) else v for v in adj_list]

    if not seed is None:
        random.seed(seed)

    for i in range(0, len(graph) - 2):

        if verbose:
            print("Graph: %s" % graph)

        # choose vertices to merge
        v_super = random.sample(graph.keys(), 1)[0]
        v_merged = random.choice(graph[v_super])
        assert(v_super != v_merged) # "Loop edge selected! (%d, %d)" % (v_super, v_merged))
        merged_list = graph.pop(v_merged)

        if verbose:
            print("Merge edge: (%d, %d)" % (v_super, v_merged))

        # merge vertices
        graph[v_super] = [v for v in (graph[v_super] + merged_list) if (v != v_super and v != v_merged)]


        for v in graph.keys():
            graph[v] = rename_vertex(graph[v], v_super, v_merged)

    assert(len(graph) == 2) # "There are %d vertices left after contaction!" % len(graph))

    cut_count = len(next(iter(graph.values())))

    all_test = [len(adj_list) == cut_count for adj_list in graph.values()]

    assert(all(all_test)) # "Bad contracted graph: %s" % graph)

    if verbose:
            print("Contracted graph: %s" % graph)

    return cut_count

def mincut(graph, max, seed = None, show_seed_rate = 0):
    "Computes the smallest cut of a graph by multiple contraction algorithm"

    cut_count = 0
    # repeated = 0

    while ((cut_count > max or cut_count == 0)):
        if not seed is None:
            seed += 1

        g = deepcopy(graph)
        new_cut_count = contract(g, seed = seed)



        if cut_count > new_cut_count or cut_count == 0:
            cut_count = new_cut_count
            g_min = deepcopy(g)
##        elif abs(cut_count - new_cut_count) < 2:
##            repeated += 1

        if show_seed_rate != 0 and seed % show_seed_rate == 0:
            print("Seed: %d, Mincut: %d" % (seed, cut_count))
            print("Contracted graph: %s" % g_min)

    print("Success! %d mincut for seed %d" % (cut_count, seed))

    return cut_count

