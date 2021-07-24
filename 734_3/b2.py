from collections import Counter

t = int(input())

for i in range(t):
	n, k = [int(x) for x in input().split()]
	s = [int(x) for x in input().split()]
	colors = {}

	c = Counter(s)
	colors_l = list(range(1, k + 1))

	curr_col = 0

	last_ele = None

	for let, nb in c.items():
		if nb >= k:
			colors[let] = colors_l[curr_col:] + colors_l[:curr_col] + [0] * (nb - k)
		else:
			colors[let] = colors_l[curr_col:min(curr_col + nb, len(colors_l))]
			if curr_col + nb > len(colors_l):
				colors[let] += colors_l[:(nb - (len(colors_l) - curr_col))]

			curr_col = (curr_col + nb) % k

		last_ele = let

	bl_cols = set(colors_l[:curr_col])

	to_print = ""
	for let in s:
		if len(bl_cols) > 0 and colors[let][-1] in bl_cols:
			bl_cols.remove(colors[let][-1])
			#to_print += "0 "
			print("0 ", end='')
			del colors[let][-1]
			continue
		#to_print += str(colors[let][-1]) + " "
		print(str(colors[let][-1]) + " ", end='')
		del colors[let][-1]

	print(to_print[:-1])
