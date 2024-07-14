def solution(name, yearning, photo):
    answer = []
    
    name_year_dict = {n:y for n, y in zip(name, yearning)}
    
    for p in photo:
        sum = 0
        for n in p:
            if n not in name:
                continue
            else:
                sum += name_year_dict[n]
        answer.append(sum)
    return answer