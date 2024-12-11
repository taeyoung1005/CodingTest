import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))
combi = list(combinations(cards, 3))

under_M = [sum(i) for i in combi if sum(i)<=M]
print(max(under_M))
