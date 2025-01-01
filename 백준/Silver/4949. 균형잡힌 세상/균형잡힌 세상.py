import sys

input = sys.stdin.readline

pair = {')':'(', ']':'['}

s = input().rstrip()

while s != '.':
    stack = []
    flag = True

    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')' or i == ']':
            if not stack or stack.pop() != pair[i]:
                flag = False
                break
        
    if flag and len(stack) == 0:
        print("yes")
    else:
        print("no")

    s = input().rstrip()