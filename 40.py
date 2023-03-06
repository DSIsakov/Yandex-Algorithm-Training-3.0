from collections import defaultdict

n = int(input())
m = int(input())
vertex = [-1] * m
stations = defaultdict(set)
distance = defaultdict(list)
edges = defaultdict(set)

for i in range(m):
	p = set(list(map(int, input().split()))[1:])
	for j in p:
		for k in stations[j]:
			edges[k].add(i)
			edges[i].add(k)
		stations[j].add(i)

a, b = list(map(int, input().split()))

starts = stations[a]
ends = stations[b]

for i in starts:
	vertex[i] = 0
	distance[0].append(i)

cur = 0
ma = 0
while cur <= ma:
	for v in distance[cur]:
		for next in edges[v]:
			if vertex[next] == -1:
				vertex[next] = cur + 1
				ma = cur + 1
				distance[cur+1].append(next)
	cur += 1

print(min([vertex[i] for i in ends]))