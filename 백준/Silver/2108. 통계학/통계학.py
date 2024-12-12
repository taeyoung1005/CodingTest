from collections import Counter
import sys

N = int(sys.stdin.readline().strip())
ns = [int(sys.stdin.readline().strip()) for _ in range(N)]

print(round(sum(ns)/len(ns)))
print(sorted(ns)[len(ns)//2])

cnt_dict = dict(Counter(ns))
max_value = max(cnt_dict.values())

max_keys = [key for key, value in cnt_dict.items() if value == max_value]
if len(max_keys) > 1:
    print(sorted(max_keys)[1])
else:
    print(max_keys[0])

print(max(ns)-min(ns))