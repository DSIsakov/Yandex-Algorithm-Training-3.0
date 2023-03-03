from collections import defaultdict

d = defaultdict(int)

s = input()
l = len(s)

for i in range(l):
	d[s[i]] += (l - i) * (i + 1)
	
for i in sorted(d):
	print(f'{i}: {d[i]}')