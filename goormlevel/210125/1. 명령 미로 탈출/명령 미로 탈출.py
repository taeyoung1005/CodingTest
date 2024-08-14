# 0이면 통과 가능
# 1이면 출발 위치
# 2이면 탈출 위치
# 3이면 벽

# 입력 받기
N, K = map(int, input().split())
commands = input()        # 명령어 입력

move_x = {'U': -1, 'D':1, 'L':0, 'R':0}
move_y = {'U': 0, 'D':0, 'L':-1, 'R':1}

# 보드 초기화 및 위치 탐색
board = []
start_x, start_y = None, None
# finish_x, finish_y = None, None

for y in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for x in range(len(row)):
        if row[x] == 1:
            start_x = y
            start_y = x

cnt = 0
for c in commands:
	if start_x + move_x[c] >= 0 and start_x + move_x[c] < N and start_y + move_y[c] >= 0 and start_y + move_y[c] < N and board[start_x + move_x[c]][start_y + move_y[c]] != 3:
		start_x += move_x[c]
		start_y += move_y[c]
		cnt += 1
	if board[start_x][start_y] == 2:
		break
		
if board[start_x][start_y] == 2:
	print(f"SUCCESS {cnt}")
else:
	print("FAIL")