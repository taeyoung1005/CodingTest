import math

N = int(input())
A = list(map(int, input().split()))

idx = []

for i in range(2, N+1):
	
	flag = False
	
	for j in range(2, int(math.sqrt(i)) + 1):
		if i % j == 0:
			flag = True
			break
			
	if not flag:
		idx.append(i-1)

print(sum([A[i] for i in idx]))