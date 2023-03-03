a, b, c, d = 10**9, 10**9, -(10**9), -(10**9)
for _ in range(int(input())):
	p, q = list(map(int, input().split()))
	a = min(a, p)
	b = min(b, q)
	c = max(c, p)
	d = max(d, q)
	
print(a, b, c, d)