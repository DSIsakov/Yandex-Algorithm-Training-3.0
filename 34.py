from collections import defaultdict
import sys

sys.setrecursionlimit(2**31-1)

n, m = list(map(int, input().split()))
vertex = defaultdict(int)
edges = defaultdict(set)

for i in range(m):
	a, b = list(map(int, input().split()))
	edges[a].add(b)
	
ans = []

def dfs(cur):
	for next in edges[cur]:
		if vertex[next] == 1:
			return False
		elif vertex[next] == 0:
			vertex[next] = 1
			res = dfs(next)
			if not res:
				return False
	vertex[cur] = 2
	ans.append(cur)
	return True

res = True
for i in range(1, n+1):
	if not vertex[i]:
		vertex[i] = 1
		res = dfs(i)
		if not res:
			print(-1)
			break

if res:
	print(*ans[::-1])