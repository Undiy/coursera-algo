import twosat

def run_twosat():
    # graph = twosat.load_implication_graph("2sat1.txt")
    # graph_rev = twosat.reversed_graph(graph)

    ans = 0

    edges = twosat.load_implication_edges("2sat1.txt")
    ans += int(twosat.is_solvable(edges))

    ans *= 10

    edges = twosat.load_implication_edges("2sat2.txt")
    ans += int(twosat.is_solvable(edges))

    ans *= 10

    edges = twosat.load_implication_edges("2sat3.txt")
    ans += int(twosat.is_solvable(edges))

    ans *= 10

    edges = twosat.load_implication_edges("2sat4.txt")
    ans += int(twosat.is_solvable(edges))

    ans *= 10

    edges = twosat.load_implication_edges("2sat5.txt")
    ans += int(twosat.is_solvable(edges))

    ans *= 10

    edges = twosat.load_implication_edges("2sat6.txt")
    ans += int(twosat.is_solvable(edges))

    print ans

def main():
    run_twosat()

if __name__ == '__main__':
    main()
