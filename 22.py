from collections import defaultdict

n, k = list(map(int, input().split()))
d = defaultdict(int)
d[0] = 1
for i in range(1, n):
	for j in range(1, k+1):
		if i - j < 0:
			break
		d[i] += d[i-j]

print(d[n-1])