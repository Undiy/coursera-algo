import cluster
import hamming
import itertools

def run_cluster():

    nodes, edges = cluster.load("clustering1.txt")

    k = 4
    n = cluster.max_cluster_spacing(nodes, edges, k)

    print "%d max spacing between %d clusters" % (n, k)

def run_hamming():
    nodes, radix = hamming.load("clustering_big.txt")
    k = hamming.count_hamming_clusters(nodes, radix, 3)
    print k

def main():
    run_cluster()
    run_hamming()

if __name__ == '__main__':
    main()
