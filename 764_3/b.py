t = int(input())

for _ in range(t):
    a, b, c = [int(x) for x in input().split()]

    # a
    if (2*b - c > 0) and (2*b - c) % a == 0:
        print("YES")
    # b
    elif (a + c > 0) and (a + c) % (2*b) == 0:
        print("YES")
    elif (2*b - a > 0) and (2*b - a) % c == 0:
        print("YES")
    else:
        print("NO")
