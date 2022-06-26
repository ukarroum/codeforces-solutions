from math import ceil

t = int(input())

for _ in range(t):
    l, r, k  = [int(x) for x in input().split()]

    if l == 1 and r == 1:
        print("NO")
    elif l == r:
        print("YES")
    elif (r - l + 1) - k <= 1:
        print("YES")
    elif r % 2 == 0 and ((r - l + 1)//2) <= k:
        print("YES")
    elif r % 2 == 1 and ceil((r - l + 1)/2) <= k:
        print("YES")
    else:
        print("NO")
