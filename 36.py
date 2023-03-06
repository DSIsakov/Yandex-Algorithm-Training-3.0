from collections import defaultdict

n = int(input())
edges = defaultdict(set)
distance = defaultdict(list)
used = set()

for i in range(n):
	raw = list(map(int, input().split()))
	for j in range(i+1):
		if raw[j]:
			edges[i+1].add(j+1)
			edges[j+1].add(i+1)

start, end = list(map(int, input().split()))
distance[0].append(start)
used.add(start)

cur = 0
m = 0
flag = True
while cur <= m and flag:
	for v in distance[cur]:
		if v == end:
			print(cur)
			flag = False
			break
		for next in edges[v]:
			if next not in used:
				distance[cur+1].append(next)
				m = cur + 1
				used.add(next)
	cur += 1

if flag:
	print(-1)