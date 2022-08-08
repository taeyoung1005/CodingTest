N = int(input())
n = 2**N - 1

def hanoi(n, start, middle, end):
    if n == 1:
        print(start, end)
        return
    hanoi(n-1, start, end, middle)
    print(start, end)
    hanoi(n-1, middle, start, end)
    
print(n)
hanoi(N, 1, 2, 3)