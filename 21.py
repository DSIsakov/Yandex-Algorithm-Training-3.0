from collections import defaultdict

n = int(input())
d = defaultdict(int)
d[-1] = 1
for i in range(n+1):
	d[i] = d[i-1] + d[i-2] + d[i-3]
	
print(d[n])