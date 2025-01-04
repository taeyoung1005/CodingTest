import sys
input = sys.stdin.readline

N = int(input().strip())
img = [list(map(int, input().strip())) for _ in range(N)]

def quadtree(size, x, y):
    value = img[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if img[i][j] != value:
                break
        else:
            continue
        break
    else:
        return str(value)

    half = size // 2
    lt = quadtree(half, x, y)
    rt = quadtree(half, x, y + half)
    lb = quadtree(half, x + half, y)
    rb = quadtree(half, x + half, y + half)
    return f'({lt}{rt}{lb}{rb})'

print(quadtree(N, 0, 0))