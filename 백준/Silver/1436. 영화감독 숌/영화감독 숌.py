import sys

N = int(sys.stdin.readline())

num = 0
cnt = 0
while True:
    num += 1
    if '666' in str(num):
        cnt += 1
    
    if cnt == N:
        print(num)
        break