# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
first_input, last_input = map(str, input().split())

operator = ['+', '*', '-']


def make_math_exp(math_exp:str):
	temp = ""
	stack = []
	for i in math_exp:
		if i in operator:
			stack.append(temp)
			stack.append(i)
			temp = ""
		else:
			temp += i
	stack.append(temp)
	
	return stack

def calc_mul_math_exp(math_exp:list):
	stack = []
	for i in math_exp:
		if stack and stack[-1] == '*':
			stack.pop()
			stack.append(int(i) * int(stack.pop()))
		else:
			stack.append(i)
	
	return stack

def calc_other_math_exp(math_exp:list):
	stack = []
	for i in math_exp:
		if stack and stack[-1] == '-':
			stack.pop()
			stack.append((int(i) - int(stack.pop()))*-1)
			
		elif stack and stack[-1] == '+':
			stack.pop()
			stack.append(int(i) + int(stack.pop()))
			
		else:
			stack.append(i)
	
	return stack

temp1 = calc_other_math_exp(calc_mul_math_exp(make_math_exp(first_input)))[0]
temp2 = calc_other_math_exp(calc_mul_math_exp(make_math_exp(last_input)))[0]

print(temp1 if temp1 > temp2 else temp2)