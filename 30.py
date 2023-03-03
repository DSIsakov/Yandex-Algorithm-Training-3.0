n = int(input())
sn = list(map(int, input().split()))
m = int(input())
sm = list(map(int, input().split()))

mat = [[0] * m for i in range(n)]

for j in range(m):
	if sn[0] == sm[j]:
		mat[0][j] = 1
	elif j == 0:
		continue
	else:
		mat[0][j] = mat[0][j-1]

for i in range(n):
	if sm[0] == sn[i]:
		mat[i][0] = 1
	elif i == 0:
		continue
	else:
		mat[i][0] = mat[i-1][0]
		
for i in range(1, n):
	for j in range(1, m):
		if sn[i] == sm[j]:
			mat[i][j] = mat[i-1][j-1] + 1
		else:
			mat[i][j] = max(mat[i-1][j], mat[i][j-1])


x, y = n-1, m-1
seq = []

while x > 0 and y > 0:
	if sn[x] == sm[y] and mat[x][y] == mat[x-1][y-1] + 1:
		seq.append(sn[x])
		x -= 1
		y -= 1
	elif mat[x-1][y] > mat[x][y-1]:
		x -= 1
	else:
		y -= 1
		
while x >= 0 and y == 0:
	if sn[x] == sm[y]:
		seq.append(sn[x])
		y -= 1
		x -= 1
		break
	x -= 1
		
while y >= 0 and x == 0:
	if sn[x] == sm[y]:
		seq.append(sm[y])
		x -= 1
		y -= 1
		break
	y -= 1

print(*seq[::-1])