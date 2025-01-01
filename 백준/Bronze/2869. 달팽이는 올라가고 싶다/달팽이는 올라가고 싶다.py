import sys

input = sys.stdin.readline

A, B, V = map(int, input().split())

temp = (V-B) // (A-B)
if (V-B) % (A-B) == 0:
    print(temp)
else:
    print(temp + 1)