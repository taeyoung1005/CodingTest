import sys

N = int(sys.stdin.readline())

result = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key=lambda x: (x[0], x[1]))

for i in result:
    print(f'{i[0]} {i[1]}')