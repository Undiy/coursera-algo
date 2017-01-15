import heapq

def load(file):
    things = list()
    file = open(file)

    size = int(file.next().split()[0])

    for line in file:
        l = line.split()
        things.append( (int(l[0]), int(l[1])) )
    file.close()

    return size, things

def max_value(size, things):

    count = len(things)

    table = dict()

    # for i in xrange(0, count + 1):
    #     table[i] = dict()

    things_heap = [(-value, weight) for value, weight in things]

    heapq.heapify(things_heap)

    total_weight = 0

    for i in xrange(0, count):

        new_table = dict()

        # value, weight = things[i]
        value, weight = heapq.heappop(things_heap)
        value = -value

        for x in xrange(0, weight):
            if x in table:
                new_table[x] = table[x]

        for x in xrange(weight, size + 1):

            p1 = 0 if not x in table else table[x]

            diff = x - weight
            p2 = 0 if not diff in table else table[diff]
            p2 += value

            if p2 > p1 and x == size:
                total_weight += weight

            p = max(p1, p2)
            if p > 0:
                new_table[x] = max(p1, p2)


        print("Item %d of %d" % (i + 1, count))

        table = new_table
        if total_weight == size:
            print "Boom!"
            break

        # print("---------")
        # print(value, weight)
        # for weight in table:
        #     print("%d: %s" % (weight, table[weight]))



    return table[size]







