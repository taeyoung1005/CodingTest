import sys

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    R, S = map(str, input().split())
    print("".join(i*int(R) for i in S))