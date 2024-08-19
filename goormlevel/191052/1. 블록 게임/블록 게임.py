# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque

direction = {'U':[-1, 0], 'D': [1, 0], 'L':[0, -1], 'R':[0, 1]}

N = input()
D = [i for i in input()]
score = list(map(int, input().split()))

path = []

result = []
sx, sy = 0, 0

path.append((sx, sy))
result.append(1)

for di, si in zip(D, score):
	x, y = sx + direction[di][0], sy + direction[di][1]
	if (x, y) in path:
		idx = path.index((x, y))
		path = path[:idx]
		result = result[:idx]
	path.append((x, y))
	result.append(si)
	
	sx, sy = x, y
	
print(sum(result))