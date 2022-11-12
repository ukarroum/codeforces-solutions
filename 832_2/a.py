t = int(input())

for _ in range(t):
	n = int(input())

	a = [int(x) for x in input().split()]

	neg = -sum([int(x) for x in a if x < 0])
	pos = sum([int(x) for x in a if x > 0])

	print(max(neg, pos) - min(neg, pos))
