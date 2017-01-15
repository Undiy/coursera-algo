import itertools
import math

def load_points(file):

    points = list()
    n = 0

    for line in open(file):
        l = line.split()
        if len(l) > 1:
            points.append( (float(l[0]), float(l[1])) )
        else:
            n = int(l[0])

    return points

def dist( (x1, y1), (x2, y2) ):
    return math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )

def make_graph(points):

    # graph = dict()

    n = len(points)
    graph = l = [None] * n
    for i in xrange(0, n):
        graph[i] = [None] * n
        graph[i][i] = 0

    # def add_vertex(graph, v):
    #     if not v in graph:
    #         graph[v] = [0] * len(points)

    for edge in itertools.combinations(xrange(0, len(points)), 2):


        v = edge[0]
        u = edge[1]
        d = dist( points[v], points[u] )
        # add_vertex(graph, v)
        # add_vertex(graph, u)
        graph[v][u] = d
        graph[u][v] = d

    # print graph

    return graph


def max_edge(graph):
    return max( graph[v][u] for v, u in itertools.combinations(xrange(0, len(graph)), 2) )

def tsp(graph):

    # def get_from_A(A, s, j, k, n):
    #     s ^= 1 << j
    #
    #     if k == 0:
    #         return 0 if s == 1 else  float('+inf')
    #     else:
    #         return A[s | k << n]


    def generate_s_list(m, n):
        # s_list = []
        # # s_map = dict()
        #
        # for i_list in itertools.combinations(xrange(1, n), m):
        #     s = 1
        #     for i in i_list:
        #         s |= 1 << i
        #
        #     # s_map[s - 1] = i_list
        #     # s_map[s] = (0,) + i_list
        #
        #     s_list.append(s)
        #
        # return s_list

        return ( 1 + sum(1 << i for i in i_list)  for i_list in itertools.combinations(xrange(1, n), m) )

    def rebuild_s(s, n):
        return (i for i in xrange(0, n) if s & 1 << i)


    def build_s(s_number, n, m, zero):

        comb = itertools.combinations(xrange(1, n), m)
        for i in xrange(0, s_number):
            comb.next()
        if zero:
            return (0, ) + comb.next()
        else:
            return comb.next()

    def get_s_num(s, j, comb):
        s = list(s)
        s.remove(j)
        s = tuple(s)

        for i in xrange(0, len(comb)):
            if comb[i] == s:
                return i

    n = len(graph)

    # max_val = max_edge(graph) * n
    max_val = float("+inf")

    fn = math.factorial(n - 1)
    fm = math.factorial((n - 1) / 2)
    fnm = math.factorial((n - 1) - (n - 1)/2)

    A_size = (fn / (fm * fnm))

    # A = [None] * A_size
    # for i in xrange(0, A_size):
    #     A[i] = [max_val] * n




    for m in xrange(1, n):

        # A_new = dict()
        point_sets = generate_s_list(m, n)
        # psl = math.factorial(n - 1) / (math.factorial(m) * math.factorial(n - 1 - m))
        comb_new = tuple(itertools.combinations(xrange(1, n), m))

        psl = len(comb_new)
        # print m, n - 1
        # print bin(n)
        # print bin(psl)
        # print "Current: %d" % psl

        count_ps = 0

        A_new = [None] * psl
        for i in xrange(0, psl):
            A_new[i] = [max_val] * (n)

        for s_num in xrange(0, psl):
            # s = build_s(s_num, n, m, False)
            s = comb_new[s_num]
            for j in s:
                for k in (0,) + comb_new[s_num]:
                    if k == j:
                        continue

                    if m == 1:
                        if k == 0 and s[0] == j:
                            A_new[s_num][j] = graph[k][j]
                    else:
                        s_j = list(s)
                        s_j.remove(j)
                        s_j = tuple(s_j)
                        A_new[s_num][j] = min(A_new[s_num][j], A[comb_map[s_j]][k] + graph[k][j])



            count_ps += 1
            #
            # percentage = float(count_ps) * 100 / len(point_sets)
            #
            if count_ps % 10000 == 0:
                 print 'Points set size: %d of %d: %d of %d [%f%%]' % (m + 1, n, count_ps, psl, count_ps * 100.0 / psl)

        print 'Points set size: %d of %d done!' % (m + 1, n)

        A = A_new
        comb_map = { s:i for i, s in enumerate(comb_new) }

    return min ( A[0][j] + graph[j][0] for j in xrange(1, n) )