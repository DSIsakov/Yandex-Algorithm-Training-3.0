from collections import defaultdict
import sys


n, m = list(map(int, input().split()))
edges = defaultdict(set)
vertex = defaultdict(int)

sys.setrecursionlimit(2**31-1)
for i in range(m):
	a, b = list(map(int, input().split()))
	edges[a].add(b)
	edges[b].add(a)


def dfs(cur):
	for next in edges[cur]:
		if not vertex[next]:
			vertex[next] = 3 - vertex[cur]
			res = dfs(next)
			if not res:
				return False
		elif vertex[next] == vertex[cur]:
			return False
	return True

res = True
for i in sorted(edges):
	if not vertex[i]:
		vertex[i] = 1
		res = dfs(i)
		if not res:
			print('NO')
			break

if res:
	print('YES')