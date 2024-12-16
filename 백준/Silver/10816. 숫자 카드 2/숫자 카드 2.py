import sys
from collections import Counter

input = sys.stdin.read

data = input().splitlines()

# 입력 처리
N = int(data[0])
cards = map(int, data[1].split())
M = int(data[2])
query = map(int, data[3].split())

cards_count = Counter(cards)

print(" ".join(str(cards_count[q]) if q in cards_count else '0' for q in query))