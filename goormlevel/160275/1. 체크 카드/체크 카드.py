from collections import deque

N, M = map(int, input().split())

credit_payment = deque()

for _ in range(M):
	money_type, amount = input().split()
	amount = int(amount)
	
	if money_type == "deposit":
		N += amount
		
		while credit_payment and N >= credit_payment[0]:
			N -= credit_payment.popleft()
			
	elif money_type == "reservation":
		if not credit_payment and N >= amount:
			N -= amount
		else:
			credit_payment.append(amount)
			
	elif money_type == "pay" and N >= amount:
		N -= amount
		
print(N)