from collections import Counter

def solution(X, Y):
    answer = ''
    
    count_x = Counter(X)
    count_y = Counter(Y)
    
    temp = count_x & count_y
    if len(temp) == 0:
        return "-1"
    elif len(temp) == 1 and temp.most_common()[0][0] == '0':
        return "0"
    else:
        for x, y in sorted(temp.items(), reverse=True):
            answer += str(x) * y
        return answer