from collections import deque

def solution(begin, target, words):
    
    words_len = len(words)
    
    queue = deque([(begin, 0)])
    
    visited = [0 for i in range(words_len)]
    
    while queue:
        word, cnt = queue.popleft()
        
        if word == target:
            return cnt
        
        for i in range(words_len):
            if not visited[i] and sum(x != y for x,y in zip(word, words[i])) == 1:
                queue.append((words[i], cnt+1))
                visited[i] = 1
        
    return 0