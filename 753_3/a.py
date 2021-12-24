t = int(input())

for _ in range(t):
    d = {c: idx for idx, c in enumerate(input())}

    s = input()

    l = [abs(d[s[i]] - d[s[i - 1]]) for i in range(1, len(s))]

    if l:
        ans = sum(l)
    else:
        ans = 0

    print(ans)


