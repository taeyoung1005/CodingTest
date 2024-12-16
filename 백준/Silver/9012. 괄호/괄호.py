import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    stack = []
    is_valid = True

    for j in input():
        if j == '(':
            stack.append(j)
        elif j == ')':
            if j == ')' and len(stack) == 0:
                is_valid = False
                break
            stack.pop()

    if is_valid and len(stack) == 0:
        print("YES")
    else:
        print("NO")