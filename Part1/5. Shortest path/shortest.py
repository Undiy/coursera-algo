import heapq

def shortest_path(graph, source):

    shortest_paths = dict()

    heap = [(0, source)]

    vertices = set(graph.iterkeys())

    # idle_steps = dict()

    while heap:
        (length, tail) = heapq.heappop(heap)

        if tail in vertices:

            shortest_paths[tail] = length
            vertices.remove(tail)

            for (head, edge_length) in graph[tail]:
                if head in vertices:

                    head_length = length + edge_length

                    if (not head in shortest_paths) or (shortest_paths[head] > head_length):
                        # heapq.heappush(heap, (length + edge_length, head))
                        heap.append((length + edge_length, head))
                        shortest_paths[head] = head_length

            heapq.heapify(heap)

    #     else:
    #         if tail in idle_steps:
    #             idle_steps[tail] += 1
    #         else:
    #             idle_steps[tail] = 1
    #
    # print(idle_steps)
    #
    # print(sum(idle_steps.itervalues()))

    return shortest_paths