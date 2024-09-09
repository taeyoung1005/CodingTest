# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = input()
temp = sum([int(i) for i in input().split()])
print(oct(temp).removeprefix('0o'))