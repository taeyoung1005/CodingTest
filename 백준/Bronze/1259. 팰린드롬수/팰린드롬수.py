import sys

while True:
    n = sys.stdin.readline().strip()
    if n == '0':break
    
    if len(n) % 2 == 0 and n[:len(n)//2] == n[len(n):len(n)//2-1:-1]:
        print("yes")
    elif len(n) % 2 == 1 and n[:len(n)//2] == n[len(n):len(n)//2:-1]:
        print("yes")
    else:
        print("no")