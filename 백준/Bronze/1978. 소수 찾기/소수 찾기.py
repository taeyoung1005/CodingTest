N = int(input())

num_list = list(map(int, input().split()))
result = 0

for i in num_list:
    if i == 1: continue

    cnt = 0
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
    
    if cnt == 0:
        result += 1

print(result)