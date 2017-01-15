
def qiucksort(array, pivot=0):
    "Quick sort algorithm in-place"

    def swap(i, j):
        if i != j:
            array[i], array[j] = array[j], array[i]

    def partition(start, end, p): # p - pivot index
        swap(start, p)

        p = start

        for i in range(start + 1, end + 1):
##            print(array)
##            print("i = %d, p = %d" % (i, p))
            if (array[i] < array[start]):
                p += 1
                swap(i, p)

        swap(p, start)
##        print(array)
        return p

    def choose_pivot(start, end):
        if pivot == 1 or (end - start < 2):
            return start
        elif pivot == 2:
            return end
        else:
            candidates = {}


            candidates[array[start]] = start

            if array[end] in candidates:
                return end
            candidates[array[end]] = end

            med = (end + start) // 2
            if array[med] in candidates:
                return med
            candidates[array[med]] = med

            candidates.pop(max(candidates))
            candidates.pop(min(candidates))
            return candidates.popitem()[1]

    def quicksort(start, end, c_count):
        if (end - start < 1):
            return 0
        p = choose_pivot(start, end)
        c_count_local = (end - start)
##        print("Pivot: %d, Count: %d" % (p, c_count))
        p = partition(start, end, p)
        c_count = quicksort(start, p - 1, c_count) + quicksort(p + 1, end, c_count) + c_count_local
##        print("Count: %d" % (c_count))
        return c_count

    return quicksort(0, len(array) - 1, 0)

