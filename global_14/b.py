t = int(input())

for i in range(t):
	n = int(input())

	if (n & (n - 1) == 0) and n != 1:
		print("YES")
	else:
		print("NO")
