n, m, k = list(map(int, input().split()))
mat = []
for i in range(n):
	raw = list(map(int, input().split()))
	mraw = []
	for j in range(m):
		x = raw[j]
		if i > 0:
			x += mat[i-1][j]
		if j > 0:
			x += mraw[j-1]
		if i > 0 and j > 0:
			x -= mat[i-1][j-1]
		mraw.append(x)
	mat.append(mraw)

for i in range(k):
	x1, y1, x2, y2 = list(map(lambda x: int(x) - 1, input().split()))
	if x1 == 0 and y1 == 0:
		x = mat[x2][y2]
	elif x1 == 0:
		x = mat[x2][y2] - mat[x2][y1-1]
	elif y1 == 0:
		x = mat[x2][y2] - mat[x1-1][y2]
	else:
		x = mat[x2][y2] - mat[x1-1][y2] - mat[x2][y1-1] + mat[x1-1][y1-1]
	print(x)