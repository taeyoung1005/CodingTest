import sys

input = sys.stdin.readline

n = int(input().strip())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    prev2, prev1 = 1, 2
    for _ in range(3, n+1):
        curr = (prev1 + prev2) % 15746
        prev2, prev1 = prev1, curr
    print(prev1)