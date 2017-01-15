import floyd_warshall

def run_floyd_warshall():

    def min_path(file):
        n, m, edges = floyd_warshall.load_edges(file)
        graph = floyd_warshall.make_graph(edges)
        A = floyd_warshall.apsp(graph)
        return floyd_warshall.min_path(A)

    min_pathes = list()

    min_pathes.append(min_path("g1.txt"))

    print(min_pathes)

    min_pathes.append(min_path("g2.txt"))

    print(min_pathes)

    min_pathes.append(min_path("g3.txt"))

    print(min_pathes)

def main():
    run_floyd_warshall()

if __name__ == '__main__':
    main()
