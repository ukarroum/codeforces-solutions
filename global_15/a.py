t = int(input())

for i in range(t):
	n = int(input())

	s = list(input())

	print(n - sum([x == y for x, y in zip(sorted(s), s)]))
