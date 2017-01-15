import jobs
import prim

def run_jobs():
    jobs_list = list()
    file = open("jobs.txt")
    for line in file:
        l = line.split()
        if len(l) > 1:
            jobs_list.append( (int(l[0]), int(l[1])) )
    file.close()

    print(sum(jobs.schedulde_by_diff(jobs_list)))
    print(sum(jobs.schedulde_by_ratio(jobs_list)))

def run_prim():
    edges = list()
    file = open("edges.txt")
    for line in file:
        l = line.split()
        if len(l) > 2:
            edges.append( tuple( int(token) for token in l ) )
    file.close()
    graph = prim.make_graph(edges)

    print("Edges: %d Vertices: %d" % (len(edges), len(graph)))

    msp = prim.prims_msp(graph)

    print( "MSP. Length: %d, Cost: %d" % (len(msp), prim.weight(msp)) )

def main():
    # run_jobs()
    run_prim()


if __name__ == '__main__':
    main()
