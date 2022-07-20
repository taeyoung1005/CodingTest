N = int(input())
if 1<=N<=1000000:
    L = list(map(int, input().split(" ")))
    print(min(L), max(L))