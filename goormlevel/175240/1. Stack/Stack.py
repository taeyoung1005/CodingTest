# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, K = map(int, input().split())

temp = []

for _ in range(N):
	user_input = input().split()
	
	if user_input[0] == "push":
		if len(temp) == K:
			print("Overflow")
			continue
		temp.append(user_input[1])
		
	else:
		if len(temp) == 0:
			print("Underflow")
			continue
		print(temp.pop())