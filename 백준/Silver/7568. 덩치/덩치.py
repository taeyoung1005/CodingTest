import sys

N = int(sys.stdin.readline())

result = [1]*N

p = [list(map(int, sys.stdin.readline().split()))  for _ in range(N)]

for i in range(N):
    for j in range(N):
        if p[i][0] > p[j][0] and p[i][1] > p[j][1]:
            result[j] += 1

print(" ".join(map(str, result)))