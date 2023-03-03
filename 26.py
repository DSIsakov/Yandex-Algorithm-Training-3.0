n, m = list(map(int, input().split()))
mat = []
mat.append(list(map(int, input().split())))
for j in range(1, m):
	mat[0][j] += mat[0][j-1]
for i in range(1, n):
	mat.append(list(map(int, input().split())))
	mat[i][0] += mat[i-1][0]
	for j in range(1, m):			
		mat[i][j] += min(mat[i][j-1], mat[i-1][j])
		
print(mat[n-1][m-1])