import sys
input = sys.stdin.readline

N = int(input().strip())

img = [list(map(int, input().split())) for _ in range(N)]

def pooling(size, x, y):
    half = size//2

    if size == 2:
        result = [img[x][y], img[x+1][y], img[x][y+1], img[x+1][y+1]]
        result.sort()

        return result[-2]
    
    lt = pooling(half, x, y)
    rt = pooling(half, x+half, y)
    lb = pooling(half, x, y+half)
    rb = pooling(half, x+half, y+half)

    result = [lt, rt, lb, rb]
    result.sort()
    return result[-2]

print(pooling(N, 0, 0))