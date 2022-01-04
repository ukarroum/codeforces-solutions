t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]

    if k > int(n / 2) + n % 2:
        print(-1)
    else:
        pr = []
        for i in range(k):
            pos = (i * 2) % n
            pr.append("."*pos + "R" + "."*(n - pos - 1))
            pr.append("."*n)
        for i in range(n - 2*k):
            pr.append("."*n)

        if n + 1 == 2*k:
            pr = pr[:-1]

        print("\n".join(pr))
