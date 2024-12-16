import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

cards = deque(range(1, N + 1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])