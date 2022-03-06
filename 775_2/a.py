t = int(input())

for _ in range(t):
    input()

    a = input().split()

    try:
        b = a.index('0') - 1
        e = len(a) - a[::-1].index('0')

        print(e - b)
    except:
        print(0)
