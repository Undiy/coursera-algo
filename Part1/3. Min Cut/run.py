import mincut

def main():
    graph = dict()
    file = open("kargerMinCut.txt")
    for line in file:
        l = line.split()
        v = int (l.pop(0))
        graph[v] = [ int(x) for x in l ]
    file.close()
    #3396 20
    mincut.mincut(graph, seed = 0, max = 17, show_seed_rate=5)

if __name__ == '__main__':
    main()
