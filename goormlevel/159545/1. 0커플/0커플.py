# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
people = set(map(int, input().split()))

pair_people = set()

for i in range(len(people)//2):
	temp = people.pop()
	if -temp in people:
		people.discard(temp)
		people.discard(-temp)
	else:
		people.add(temp)
		
print(sum(people))