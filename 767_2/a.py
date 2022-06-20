t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]

    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    ram = sorted(zip(a, b), key=lambda x: x[0])

    for ai, bi in ram:
        if ai <= k:
            k += bi

    print(k)
    
