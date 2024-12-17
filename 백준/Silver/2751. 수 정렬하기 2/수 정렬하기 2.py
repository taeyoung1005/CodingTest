import sys

N = int(sys.stdin.readline())

for j in sorted([int(sys.stdin.readline()) for i in range(N)]):
    print(j)