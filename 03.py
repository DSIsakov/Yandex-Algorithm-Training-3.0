def binsearch(stickers: list, left: int, right: int, value: int):
	mid = (right + left) // 2
	if right - left < 2:
		if value == stickers[left]:
			return left
		else:
			return right
	if value > stickers[mid]:
		return binsearch(stickers, mid, right, value)
	elif value < stickers[mid]:
		return binsearch(stickers, left, mid, value)
	else:
		return mid
		
		
n = int(input())
stickers = sorted(set(list(map(int, input().split()))))
k = int(input())
p = list(map(int, input().split()))

for i in p:
	if i < stickers[0]:
		print(0)
	elif i > stickers[-1]:
		print(len(stickers))
	else:
		mid = binsearch(stickers, 0, len(stickers)-1, i)
		print(mid)