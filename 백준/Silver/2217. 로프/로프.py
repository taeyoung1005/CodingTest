import sys

input = sys.stdin.readline

N = int(input().rstrip())

rope = [int(input().rstrip()) for _ in range(N)]
rope.sort()

print(max([rope[i]*(N-i) for i in range(N)]))