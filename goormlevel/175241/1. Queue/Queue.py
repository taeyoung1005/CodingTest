# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, K = map(int, input().split())

queue = []
for i in range(N):
	user_input = input().split()
	
	if user_input[0] == "push":
		if len(queue) >= K:
			print("Overflow")
			continue
		queue.append(user_input[1])
	else:
		if len(queue) == 0:
			print("Underflow")
			continue
		print(queue.pop(0))
	