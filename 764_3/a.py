t = int(input())

for _ in range(t):
    n = int(input())

    l = [int(x) for x in input().split()]

    print(max(l) - min(l))
