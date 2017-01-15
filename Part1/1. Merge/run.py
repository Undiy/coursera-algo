import mergesort

def main():
    a = []
    file = open("IntegerArray.txt")
    for line in file:
        a.append(int(line))
    file.close
    a_s, count = mergesort.mergesortcount(a)
    print(a_s)
    print(count)
    print(a_s == sorted(a))

if __name__ == '__main__':
    main()
