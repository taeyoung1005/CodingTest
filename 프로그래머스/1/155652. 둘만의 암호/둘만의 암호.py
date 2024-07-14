def solution(s, skip, index):
    answer = ""
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    skip_set = set(skip)

    filtered_alpha = ''.join([char for char in alpha if char not in skip_set])

    char_to_index = {char: idx for idx, char in enumerate(filtered_alpha)}
    index_to_char = {idx: char for idx, char in enumerate(filtered_alpha)}
    filtered_alpha_length = len(filtered_alpha)

    for char in s:
        current_index = char_to_index[char]
        new_index = (current_index + index) % filtered_alpha_length
        answer += index_to_char[new_index]

    return answer