import sys

N = int(sys.stdin.readline())
origin_scores = list(map(int, sys.stdin.readline().split()))

max_score = max(origin_scores)
new_scores = [i/max_score*100 for i in origin_scores]
    
print(sum(new_scores) / len(new_scores)) 