t = int(input())

for i in range(t):
	n = int(input())

	base = int(n / 3)

	if n % 3 == 1:
		print(f"{base + 1} {base}")
	elif n % 3 == 2:
		print(f"{base} {base + 1}")
	else:
		print(f"{base} {base}")
	
