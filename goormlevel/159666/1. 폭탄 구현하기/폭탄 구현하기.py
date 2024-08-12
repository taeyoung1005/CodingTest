# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

N, K = map(int, input().split())

ground = [[0] * N for _ in range(N)]

for _ in range(K):
    y, x = map(int, input().split())
    
		# 인덱스 조정
    y -= 1
    x -= 1
    
    ground[x][y] += 1
    
		# x가 맨 왼쪽 열이 아닐 때
    if x > 0:
        ground[x-1][y] += 1
		
		# x가 맨 오른쪽 열이 아닐 때
    if x < N-1:
        ground[x+1][y] += 1
		
		# y가 맨 위쪽 행이 아닐 떄
    if y > 0:
        ground[x][y-1] += 1
				
		# y가 맨 아래쪽 행이 아닐 때
    if y < N-1:
        ground[x][y+1] += 1

total = sum(sum(row) for row in ground)

print(total)
