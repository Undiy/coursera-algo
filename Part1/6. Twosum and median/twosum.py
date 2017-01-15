def twosum_exists(numbers, sum):
    for number in numbers:
        if sum - number in numbers:
            print("%d + %d = %d" % (number, sum - number, sum))
            return True
    return False

def twosum_count(numbers, sums):

    def sum_of_neg_and_pos(numbers_pos, numbers_neg, sum):
        for n_pos in numbers_pos:
            if sum - n_pos in numbers_neg:
                print("%d + %d = %d" % (n_pos, sum - n_pos, sum))
                return True
        return False

    def sum_of_negs_or_poss(numbers_pos, numbers_neg, sum):
        if sum > 0:
            numbers = numbers_pos
        else:
            numbers = numbers_neg

        for n in numbers:
            if abs(sum) > abs(n) and sum - n in numbers:
                print("%d + %d = %d" % (n, sum - n, sum))
                return True
        return False


    numbers_pos = {n for n in numbers if n > 0}
    numbers_neg = numbers.difference(numbers_pos)

    count = 0;

    for sum in sums:

        if sum_of_neg_and_pos(numbers_pos, numbers_neg, sum) or\
                sum_of_negs_or_poss(numbers_pos, numbers_neg, sum):
            count += 1
            print("Count: %d; Sum: %d" % (count, sum))


    return count
#
# def twosum_count(numbers, sums):
#
#     sums_hash = {s: set() for s in sums}
#
#     for s in sums:
#         for n in numbers:
#             sums_hash[s].add(s - n)
#
#     for s in sums:
#         for n in sums_hash[s]:
#             if n in numbers:
#
#
#
#
#     return
