a1, b1, c1 = list(map(int, input().split(':')))
a2, b2, c2 = list(map(int, input().split(':')))
a3, b3, c3 = list(map(int, input().split(':')))

t1 = a1 * 3600 + b1 * 60 + c1
t2 = a2 * 3600 + b2 * 60 + c2
t3 = a3 * 3600 + b3 * 60 + c3

if t3 < t1:
	t3 += 3600 * 24

delta = (t3 - t1 + 1) // 2

t2 += delta

a4 = (t2 // 3600) % 24
b4 = (t2 % 3600) // 60
c4 = (t2 % 3600) % 60

print(f'{"0" * (2 - len(str(a4))) + str(a4)}:{"0" * (2 - len(str(b4))) + str(b4)}:{"0" * (2-len(str(c4))) + str(c4)}')
