import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())  # 정점의 개수, 간선의 개수
K = int(input().strip())  # 시작 정점의 번호

graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

result = [float('inf')] * (V+1)

def dijkstra(graph, start):
    q = []
    heapq.heappush(q, (0, start))
    result[start] = 0

    while q:
        w, v = heapq.heappop(q)

        if result[v] < w:
            continue

        for next_node, w in graph[v]:
            next_w = w + result[v]
            if next_w < result[next_node]:
                result[next_node] = next_w
                heapq.heappush(q, (next_w, next_node))

dijkstra(graph, K)

for i in range(1, V+1):
    print(result[i] if result[i] != float('inf') else 'INF')