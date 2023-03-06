from collections import defaultdict

n = int(input())

cube = []
distance = defaultdict(list)

for i in range(n):
	input()
	layer = []
	for j in range(n):
		s = input()
		raw = []
		for k in range(n):
			if s[k] == '#':
				raw.append(-2)
			elif s[k] == '.':
				raw.append(-1)
			else:
				distance[0].append((i, j, k))
				raw.append(0)
		layer.append(raw)
	cube.append(layer)
	
def getN(v):
	neighbours = []
	x, y, z = v
	for i in [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]:
		if i[0] >= 0 and i[0] < n and i[1] >= 0 and i[1] < n and i[2] >= 0 and i[2] < n:
			neighbours.append(i)
	return neighbours

cur = 0
m = 0
while cur <= m:
	for v in distance[cur]:
		if v[0] == 0:
			print(cur)
			m = -1
			break
		for next in getN(v):
			x, y, z = next
			if cube[x][y][z] == -1:
				cube[x][y][z] = cur + 1
				distance[cur+1].append(next)
				m = cur + 1
	cur += 1