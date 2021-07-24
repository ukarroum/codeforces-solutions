from collections import Counter

t = int(input())

for i in range(t):
	s = input()

	c = Counter(s)
	one_ele = []
	two_ele = []

	for let, nb in c.items():
		if nb >= 2:
			two_ele.append(let)
		else:
			one_ele.append(let)

	print(len(two_ele) + int(len(one_ele)/2))
