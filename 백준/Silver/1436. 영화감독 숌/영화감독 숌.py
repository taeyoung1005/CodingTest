import sys

input = sys.stdin.readline

N = int(input())

start = 666
cnt = 0
while True:
    if cnt == N:
        print(start-1)
        break

    if '666' in str(start):
        cnt += 1
    
    start += 1