# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, M = map(int, input().split())
num_list = [i if i % M == 0 else i * M for i in list(map(int, input().split()))]

print(*num_list, sep=' ')