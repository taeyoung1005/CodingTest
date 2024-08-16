# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()

temp = {'1':0, 'I':0, 'l':0, '|':0}

for i in user_input:
	if i in temp:
		temp[i] += 1
	
for i in temp.values():
	print(i)
