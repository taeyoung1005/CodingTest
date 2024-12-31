import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

for i in sorted(set(permutations(num_list, M)), key= lambda x: ([x[i] for i in range(M)])):
    print(*i)