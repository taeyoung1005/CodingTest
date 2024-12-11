import sys

S = sys.stdin.readline().strip()

for i in 'abcdefghijklmnopqrstuvwxyz':
    try:
        print(S.index(i))
    except:
        print(-1)