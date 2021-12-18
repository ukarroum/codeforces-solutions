t = int(input())

for _ in range(t):
    s = input()

    nb_n = len([c for c in s if c == 'N'])

    if nb_n == 1 and len(s) >= 2:
        print("NO")
    else:
        print("YES")
