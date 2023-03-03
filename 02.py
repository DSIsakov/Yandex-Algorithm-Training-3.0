def count(s: str, c: str, k: int):
	tempk = k
	left = 0
	right = 0
	m = 0
	l = len(s)
	while right < l:
		if s[right] != c:
			tempk -= 1
		if tempk < 0:
			m = max(m, right - left)
			left += 1
			while s[left - 1] == c:
				left += 1
			tempk += 1
			
		right += 1
	
	return max(m, right - left)


k = int(input())
s = input()
m = 0
l = len(s)
for c in set(s):
	cnt = count(s, c, k)
	if cnt > m:
		m = cnt
	
print(m)