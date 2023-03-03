from collections import defaultdict, Counter
m = int(input())
n = int(input())
os = defaultdict(list)
active = set()

for i in range(n):
	a, b = list(map(int, input().split()))
	todelete = set()
	for j in active:
		x, y = os[j]
		if a <= x and b >= x:
			todelete.add(j)
		elif a <= y and b >= y:
			todelete.add(j)
		elif x <= a and y >= b:
			todelete.add(j)
	for j in todelete:
		active.remove(j)
	os[i] = [a, b]
	active.add(i)

print(len(active))