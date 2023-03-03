from collections import defaultdict

n = int(input())
d = defaultdict(list)
d[-3] = [0,0,0,0]
d[-2] = [0,0,3601,0]
d[-1] = [0,3601,3601,0]

for i in range(n):
	a,b,c = list(map(int, input().split()))
	d[i] = [a,b,c]
	d[i].append(min(d[i-1][3] + a, d[i-2][3] + d[i-1][1], d[i-3][3] + d[i-2][2]))
	
print(d[n-1][3])