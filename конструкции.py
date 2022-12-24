with open("1.txt") as f:
    print(f.readline())
    print(f.readlines())
    print([x for x in f])

with open("2.txt") as s:
    print(s.readline())
    print(s.readlines())
    print([x for x in s])
