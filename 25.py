from collections import defaultdict

d = defaultdict(int)

n = int(input())
l = sorted(list(map(int, input().split())))
d[0] = 100000
for i in range(1, n):
	d[i] = min(d[i-1] + l[i] - l[i-1], d[i-2] + l[i] - l[i-1])
	
print(d[n-1])