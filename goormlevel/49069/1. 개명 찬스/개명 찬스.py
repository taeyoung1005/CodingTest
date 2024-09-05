# 앞의 문자가 뒤에 문자보다 크게 없애고 종료
user_input = input()

temp = None
for i in range(len(user_input)-1):
	if user_input[i] > user_input[i+1]:
		temp = user_input[:i] + user_input[i+1:]
		break
		
if temp:
	print(temp)
else:
	print(user_input[:-1])