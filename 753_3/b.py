t = int(input())

for _ in range(t):
    x, n = [int(y) for y in input().split()]

    tmp = n % 4
    if x % 2 == 0:
        if tmp == 1:
            x -= n
        elif tmp == 2:
            x += 1
        elif tmp == 3:
            x += n + 1
    else:
        if tmp == 1:
            x += n
        elif tmp == 2:
            x -= 1
        elif tmp == 3:
            x -= (n + 1)

    print(x)
            

