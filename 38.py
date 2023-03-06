from collections import defaultdict

n, m, s, t, q = list(map(int, input().split()))
s -= 1
t -= 1

distance = defaultdict(list)
mat = [[-1] * m for _ in range(n)]

mat[s][t] = 0
distance[0].append((s, t))

def getNeighbours(x, y):
	neighbours = []
	for i in [(x-2, y-1), (x-2, y+1), (x-1, y-2), (x-1, y+2), (x+1, y-2), (x+1, y+2), (x+2, y-1), (x+2, y+1)]:
		if i[0] >= 0 and i[0] < n and i[1] >= 0 and i[1] < m:
			neighbours.append(i)
	return neighbours

cur = 0
ma = 0
while cur <= ma:
	for v in distance[cur]:
		for next in getNeighbours(v[0], v[1]):
			if mat[next[0]][next[1]] == -1:
				mat[next[0]][next[1]] = cur + 1
				distance[cur+1].append(next)
				ma = cur + 1
	cur += 1


s = 0
for _ in range(q):
	a, b = list(map(lambda x: int(x) - 1, input().split()))
	if mat[a][b] == -1:
		print(-1)
		s = -1
		break
	s += mat[a][b]

if s >= 0:	
	print(s)