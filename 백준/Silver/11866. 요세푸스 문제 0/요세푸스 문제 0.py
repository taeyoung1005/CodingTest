import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

result = "<"
people = deque(range(1, N+1))

while people:
    for i in range(K-1):
        people.append(people.popleft())
    result += str(people.popleft()) + ", "

print(result.removesuffix(", ") + ">")