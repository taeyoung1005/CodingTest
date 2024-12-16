import sys

N = int(sys.stdin.readline().strip())

for j in sorted([int(sys.stdin.readline().strip()) for i in range(N)]):
    print(j)