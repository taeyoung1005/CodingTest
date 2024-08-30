def solution(board, moves):
    answer = 0
    
    queue = []
    board_T = [[] for _ in range(len(board))]
    
    for i in reversed(board):
        for j in range(len(board)):
            if i[j] != 0:
                board_T[j].append(i[j])
    
    
    for move in moves:
        if len(board_T[move-1]) >= 1:
            temp = board_T[move-1].pop()
            queue.append(temp)

            if len(queue) >= 2 and queue[-2] == temp:
                for _ in range(2):
                    queue.pop()
                answer += 2
        
        
    return answer