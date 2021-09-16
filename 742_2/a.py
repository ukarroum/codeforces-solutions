t = int(input())

trans = {'D': 'U', 'L': 'L', 'R': 'R', 'U': 'D'}

for _ in range(t):
    _ = int(input())

    s = input()

    print(''.join([trans[c] for c in s]))
