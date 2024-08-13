# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())
문제_list = list(map(int, input().split()))

연속_flag = True
연속_중단점 = None

# 연속 확인
total = 문제_list[0]
max_num = max(문제_list)

for i in range(1, len(문제_list)):
	if 문제_list[i]-1 == 문제_list[i-1]:
		total += 문제_list[i]
	else:
		if total > max_num:
			max_num = total
		total = 문제_list[i]
print(max(total, max_num))

