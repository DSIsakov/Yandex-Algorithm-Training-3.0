n, m = list(map(int, input().split()))

mat = [[1]]
for i in range(1, m):
	mat[0].append(0)

for i in range(1, n):
	mat.append([])
	for j in range(m):
		x = 0
		if j - 2 >= 0 and i - 1 >= 0:
			x += mat[i-1][j-2]
		if j - 1 >= 0 and i - 2 >= 0:
			x += mat[i-2][j-1]
		mat[i].append(x)
		

print(mat[n-1][m-1])