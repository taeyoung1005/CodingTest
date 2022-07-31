import heapq
import sys

heap = []

N = int(input())
for i in range(N):
    X = int(sys.stdin.readline())
    if X == 0:
        if len(heap) == 0:
            print("0")
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, X)