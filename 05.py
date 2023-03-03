n = int(input())
prev = 0
count = 0
for _ in range(n):
	c = int(input())
	count += min(prev, c)
	prev = c

print(count)