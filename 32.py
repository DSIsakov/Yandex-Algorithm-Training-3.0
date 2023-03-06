from collections import defaultdict
import sys


n, m = list(map(int, input().split()))
edges = defaultdict(set)
comp = defaultdict(set)
used = set()

sys.setrecursionlimit(2**31-1)
for i in range(m):
	a, b = list(map(int, input().split()))
	edges[a].add(b)
	edges[b].add(a)

sv = 0
def dfs(cur):
	for next in edges[cur]:
		if next not in used:
			used.add(next)
			comp[sv].add(next)
			dfs(next)

for i in range(1, n+1):
	if i not in used:
		sv += 1
		used.add(i)
		comp[sv].add(i)
		dfs(i)

print(len(comp))
for i in comp.values():
	print(len(i))
	print(*i)