def solution(N, stages):
    answer = []
    
    total_player = len(stages)
    
    # [실패, 성공]
    rate = {i:0 for i in range(1, N+1)}
    
    
    for i in set(stages):
        total = fail = 0
        for j in stages:
            if j >= i:
                total += 1
            if j == i:
                fail += 1
        if i != N + 1:
            rate[i] = fail / total
    
    answer = [i[0] for i in sorted(rate.items(), key=lambda x : (-x[1], x[0]))]
    
    return answer