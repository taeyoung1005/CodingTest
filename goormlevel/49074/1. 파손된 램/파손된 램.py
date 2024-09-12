# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math

N = int(input())
M = list(map(int, input().split()))

cnt = 0
broken_ram_idx = []

for i in range(len(M)):
	if bin(M[i]).removeprefix('0b').count('1') > 1:
		cnt += 1
		broken_ram_idx.append(str(i+1))

if cnt == 0:
	print(0)
else:
	print(cnt)
	print(" ".join(broken_ram_idx))