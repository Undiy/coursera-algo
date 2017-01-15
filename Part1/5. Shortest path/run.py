import shortest

def main():

    graph = dict()
    file = open("dijkstraData.txt")
    for line in file:
        pairs = line.split()
        graph[int(pairs[0])] = [ (int(pair.split(",")[0]), int(pair.split(",")[1])) for pair in pairs[1:]]
    file.close()

    p = shortest.shortest_path(graph, 1)

    print(p)


    # for v in [7,37,59,82,99,115,133,165,188,197]:
        # if v in p:
        #     print("p[%d]=%d" % (v, p[v]))
        # else:
        #     print("p[%d]=infinity" % v)

    print(",".join(str(p[v]) for v in [7,37,59,82,99,115,133,165,188,197]))

if __name__ == '__main__':
    main()
