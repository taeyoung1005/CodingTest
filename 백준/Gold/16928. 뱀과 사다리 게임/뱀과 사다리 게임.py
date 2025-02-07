import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ladder = {}

for _ in range(N + M):
    x, y = map(int, input().split())
    ladder[x] = y


def bfs():
    queue = [1]
    visited = [0] * 101
    visited[1] = 1

    while queue:
        x = queue.pop(0)

        if x == 100:
            return visited[x] - 1

        for i in range(1, 7):
            nx = x + i

            if nx > 100:
                continue

            if nx in ladder:
                nx = ladder[nx]

            if not visited[nx]:
                visited[nx] = visited[x] + 1
                queue.append(nx)


print(bfs())