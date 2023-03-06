from collections import defaultdict
import sys


n, m = list(map(int, input().split()))
edges = defaultdict(set)

sys.setrecursionlimit(2**31-1)
for i in range(m):
	a, b = list(map(int, input().split()))
	edges[a].add(b)
	edges[b].add(a)
		
used = set()
used.add(1)

def dfs(cur):
	for next in edges[cur]:
		if next not in used:
			used.add(next)
			dfs(next)

dfs(1)

print(len(used))
print(*sorted(used))