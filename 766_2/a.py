t = int(input())

for _ in range(t):
    n, m, r, c = [int(x) for x in input().split()]

    l = []
    for i in range(n):
        l.append(input())
    
    if all(["B" not in s for s in l]):
        print(-1)
    elif l[r - 1][c - 1] == 'B':
        print(0)
    elif 'B' in l[r - 1] or any([s[c - 1] == 'B' for s in l]):
        print(1)
    else:
        print(2)

    
