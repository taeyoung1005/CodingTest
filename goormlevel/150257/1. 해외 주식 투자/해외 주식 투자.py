# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math

N = int(input())

temp = {}

for i in range(1, N+1):
	v, w = map(float, input().split())
	temp[i] = math.floor(v * w * 10) / 10
	
sorted_temp = sorted(temp.items(), key=lambda x : x[1], reverse=True)
print(" ".join(map(str, [key for key, value in sorted_temp])))