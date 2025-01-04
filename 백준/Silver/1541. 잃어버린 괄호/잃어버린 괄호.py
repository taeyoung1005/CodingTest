import sys

input = sys.stdin.readline

s = input().rstrip().split('-')

result = []
for i in s:
    result.append(sum(list(map(int, i.split('+')))))

print(result[0] - sum(result[1:]))