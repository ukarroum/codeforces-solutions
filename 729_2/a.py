t = int(input())

for i in range(t):
	n = int(input())

	nb_pairs = 0
	nb_imp = 0

	nbs = [int(x) for x in input().split()]

	for j in range(2*n):
		if nbs[j] % 2 == 1:
			nb_imp += 1
		else:
			nb_pairs += 1

	print("Yes" if nb_pairs == nb_imp else "NO")


