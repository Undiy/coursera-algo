import twosum
import median

def run_twosum():

    numbers = set()
    file = open("algo1_programming_prob_2sum.txt")
    for line in file:
        numbers.add(int(line))
    file.close()

    # count = 0
    # for sum in xrange(-1000, 1001):
    #     if twosum.twosum_exists(numbers, sum):
    #         count += 1

    count = twosum.twosum_count(numbers, xrange(-10000, 10001))

    print("Count: %d" % count)

def run_medians():
    numbers = list()
    file = open("Median.txt")
    for line in file:
        numbers.append(int(line))
    file.close()

    medians = median.median_list(numbers)

    print("Medians[%d]: %s" % (len(medians), medians))

    answer = sum(medians)

    print("Sum: %d" % answer)

def main():
    run_twosum()
    run_medians()

if __name__ == '__main__':
    main()
