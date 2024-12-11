import sys

num_list = [int(sys.stdin.readline().strip()) for _ in range(9)]
max_num = max(num_list)
print(max_num)
print(num_list.index(max_num)+1)