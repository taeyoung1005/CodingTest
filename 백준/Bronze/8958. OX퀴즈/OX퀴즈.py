import sys

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    result = 0
    s = input().strip()

    cnt = 0
    for i in s:
        if i == 'O':
            cnt += 1
        else:
            cnt = 0
        result += cnt

    print(result)