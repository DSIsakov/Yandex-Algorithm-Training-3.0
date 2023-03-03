n = int(input())

a = []
mat = [[300000] * (n+2) for i in range(n)]
if n > 0:
	first = int(input())
	a.append(first)
	if first > 100:
		mat[0][1] = first
	else:
		mat[0][0] = first
	
		
	for i in range(1, n):
		price = int(input())
		a.append(price)
		if price > 100:
			for j in range(n):
				mat[i][j] = min(mat[i-1][j-1] + price, mat[i-1][j+1])
		else:
			for j in range(n):
				mat[i][j] = min(mat[i-1][j] + price, mat[i-1][j+1])
				
	
	s, k1, k2 = 3000000, 0, 0
	
	for i in range(n+1):
		if mat[n-1][i] <= s:
			s = mat[n-1][i]
			k1 = i
	
	print(s)
	cur = k1
	used = []
	for i in range(n-1, 0, -1):
		if a[i] > 100:
			if mat[i-1][cur-1] + a[i] < mat[i-1][cur+1]:
				cur -= 1
			else:
				k2 += 1
				used.append(i+1)
				cur += 1
		else:
			if mat[i-1][cur] + a[i] > mat[i-1][cur+1]:
				k2 += 1
				used.append(i+1)
				cur += 1
				
	print(k1, k2)
	
	for i in sorted(used):
		print(i)

else:
	print(0)
	print(0, 0)