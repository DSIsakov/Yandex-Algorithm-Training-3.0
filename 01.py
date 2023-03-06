from collections import Counter
import sys

s = ''
while True:
	try:
		s += ''.join(input().split())
	except EOFError:
		break


c = Counter(s)
current = max(c.values())

while current > 0:
	line = ''
	for char in sorted(c):
		if c[char] == current:
			line += '#'
			c[char] -= 1
		else:
			line += ' '
	print(line)
	current -= 1

print(''.join(sorted(c)))