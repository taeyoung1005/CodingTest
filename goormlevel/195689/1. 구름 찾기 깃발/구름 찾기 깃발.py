N, K = map(int, input().split())

groom_list = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            groom_list[i][j] = -999999
            
            if i > 0:
                groom_list[i-1][j] += 1
            if i < N-1:
                groom_list[i+1][j] += 1
            if j > 0:
                groom_list[i][j-1] += 1
            if j < N-1:
                groom_list[i][j+1] += 1
            if i > 0 and j > 0:
                groom_list[i-1][j-1] += 1
            if i > 0 and j < N-1:
                groom_list[i-1][j+1] += 1
            if i < N-1 and j > 0:
                groom_list[i+1][j-1] += 1
            if i < N-1 and j < N-1:
                groom_list[i+1][j+1] += 1

cnt = 0
for i in groom_list:
    for j in i:
        if j == K:
            cnt += 1

print(cnt)
