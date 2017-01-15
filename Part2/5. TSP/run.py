import tsp

def run_tsp():
    points = tsp.load_points("tsp.txt")
    graph = tsp.make_graph(points)
    route = tsp.tsp(graph)
    print route

def main():
    run_tsp()

if __name__ == '__main__':
    main()
