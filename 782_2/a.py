t = int(input())

for _ in range(t):
    n, r, b = [int(x) for x in input().split()]

    d = r // (b + 1)
    m = r % (b + 1)

    s = ""
    
    print( ("R" * (d + 1) + "B")*m + ("R" * d + "B") * (b - m) + ("R" * d) )
    
