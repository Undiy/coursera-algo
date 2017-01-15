def mergesort(a):

    def merge(part1, part2):
        len_half = min(len(part1), len(part2))
        merged = []
        while part1 and part2:
            if part1[0] > part2[0]:
                merged.append(part2.pop(0))
            else:
                merged.append(part1.pop(0))

        return merged + part1 + part2

    len_half = len(a) // 2
    if (len_half < 1):
        return a
    return merge(mergesort(a[:len_half]), mergesort(a[len_half:]))

def mergesortcount(a):

    def mergecount(part1, part2):
        count = 0
        merged = []
        while part1 and part2:
            if part1[0] > part2[0]:
                merged.append(part2.pop(0))
                count += len(part1)
            else:
                merged.append(part1.pop(0))

        return (merged + part1 + part2, count)




    len_half = len(a) // 2
    if (len_half < 1):
        return a, 0
    part1, count1 = mergesortcount(a[:len_half])
    part2, count2 = mergesortcount(a[len_half:])
    merged, count3 = mergecount(part1, part2)
    return(merged, count1 + count2 + count3)



