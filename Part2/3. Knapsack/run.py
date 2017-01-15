import knapsack

def run_knapsack():
    size, things = knapsack.load("knapsack1.txt")
    print knapsack.max_value(size, things)

    size, things = knapsack.load("knapsack_big.txt")
    print knapsack.max_value(size, things)

def main():
    run_knapsack()

if __name__ == '__main__':
    main()
