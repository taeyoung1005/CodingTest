N = int(input())

def 분해합(num):
    for i in range(1, num+1):
        temp = sum([int(j) for j in str(i)])
        if temp + i == num:
            return i
    return 0

print(분해합(N))