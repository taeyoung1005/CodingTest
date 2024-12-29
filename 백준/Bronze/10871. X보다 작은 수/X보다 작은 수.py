import sys

input = sys.stdin.readline

N, K = map(int, input().split())

print(" ".join([str(i) for i in list(map(int, input().split())) if i < K ]))