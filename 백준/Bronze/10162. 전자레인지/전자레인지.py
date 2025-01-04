import sys

input = sys.stdin.readline

T = int(input().rstrip())

result = [0, 0, 0] # 300, 60, 10

if T % 10 != 0:
    print(-1)
else:
    result[0] = T // 300
    result[1] = (T % 300) // 60
    result[2] = (T % 60) // 10

    print(" ".join(map(str, result)))