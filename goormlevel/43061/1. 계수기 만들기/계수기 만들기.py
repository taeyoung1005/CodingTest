# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
K = int(input())

temp = []

for B in range(len(B_list)-1, -1, -1):
	temp.append((B_list[B] + K) % (A_list[B]+1))
	K = (B_list[B] + K) // (A_list[B]+1)

while temp:
	print(temp.pop(), end="")