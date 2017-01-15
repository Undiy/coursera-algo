import heapq

def median_list(numbers):

    min_heap = list()
    max_heap = list()
    medians = list()

    for n in numbers:
        if len(min_heap) > len(max_heap):
            
            median = heapq.heappushpop(min_heap, n)
            heapq.heappush(max_heap, -median)
            median = - max_heap[0]

        else:
            median = - heapq.heappushpop(max_heap, -n) # push and pop from maxheap
            heapq.heappush(min_heap, median) # push into minheap
            median = min_heap[0]

        medians.append(median)

    return medians
