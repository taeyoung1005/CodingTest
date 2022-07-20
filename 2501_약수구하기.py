N, K = map(int, input().split())

divisor_list = []
for i in range(1, N+1):
    if N % i == 0:
        divisor_list.append(i)
        
if len(divisor_list) < K:
    print("0")
else:
    divisor_list.sort()
    print(divisor_list[K-1])