import sys
from math import factorial

N = int(sys.stdin.readline())

cnt = 0
for i in reversed(str(factorial(N))):
    if i == '0':
        cnt += 1
    else:
        print(cnt)
        break