t = int(input())

for _ in range(t):
    w, h = [int(x) for x in input().split()]

    s = []
    min_max = []

    for i in range(4):
        s.append([int(x) for x in input().split()[1:]])
        min_max.append( (min(s[-1]), max(s[-1])) )

    max_1 = max(min_max[:2], key=lambda x: x[1] - x[0])
    max_2 = max(min_max[2:], key=lambda x: x[1] - x[0])

    print(max((max_1[1] - max_1[0]) * h, (max_2[1] - max_2[0]) * w))

    
