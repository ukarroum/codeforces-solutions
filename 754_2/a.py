import math

t = int(input())

for _ in range(t):
    a, b, c = [int(x) for x in input().split()]

    if a + c == 2*b:
        print(0)
    elif a + c < 2*b:
        print(min(1, (2*b - (a + c)) % 3))
    else:
        print(min(1, (a + c - 2*b) % 3 ))
