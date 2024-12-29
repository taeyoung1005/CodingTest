import sys

input = sys.stdin.readline

print(len(set(int(input().strip()) % 42 for _ in range(10))))