t = int(input())

for i in range(t):
	n, x = [int(xx) for xx in input().split()]

	l = sorted([ int(xx) for xx in input().split() ])

	su = 0
	for i in range(len(l)):
		su += l[i]
		if su >= x:
			break
	if i == len(l) - 1 and su == x:
		print("NO")
	elif su != x:
		print("YES")
		print(" ".join([str(xx) for xx in l]))
	else:
		print("YES")
		new_list = l[:i] + [l[i+1], l[i]] + l[i + 2:]
		print(" ".join([str(xx) for xx in new_list]))
		
