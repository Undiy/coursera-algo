import quicksort

def main():
    a = []
    file = open("QuickSort.txt")
    for line in file:
        a.append(int(line))
    file.close
    print(quicksort.qiucksort(a))
##    print(a)

if __name__ == '__main__':
    main()
