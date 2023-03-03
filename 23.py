from collections import defaultdict

n = int(input())

d = [0] * (n+1)

for i in range(2, n+1):
	a = []
	if i % 3 == 0:
		a.append(d[i//3])
	if i % 2 == 0:
		a.append(d[i//2])
	a.append(d[i-1])
	d[i] = min(a) + 1

print(d[n])

path = []
cur = n
while cur > 0:
	path.append(cur)
	if cur % 3 == 0 and d[cur] == d[cur//3] + 1:
		cur //= 3
	elif cur % 2 == 0 and d[cur] == d[cur//2] + 1:
		cur //= 2
	else:
		cur -= 1

print(*path[::-1])