from collections import defaultdict
import copy
import sys

sys.setrecursionlimit(2**31-1)

n = int(input())
vertex = defaultdict(int)
edges = defaultdict(set)

for i in range(n):
	raw = list(map(int, input().split()))
	for j in range(i+1):
		if raw[j]:
			edges[i+1].add(j+1)
			edges[j+1].add(i+1)

def dfs(cur, prev, path: list):
	for next in edges[cur]:
		if next == prev:
			continue
		if vertex[next] == 1:
			print('YES')
			ind = path.index(next)
			print(len(path[ind:]))
			print(*path[ind:])
			return True
		elif not vertex[next]:
			vertex[next] = 1
			res = dfs(next, cur, path + [next])
			if res:
				return True
	vertex[cur] = 2
	return False

res = False
for i in range(1, n+1):
	if not vertex[i]:
		vertex[i] = 1
		res = dfs(i, 0, [i])
		if res:
			break


if not res:
	print('NO')
