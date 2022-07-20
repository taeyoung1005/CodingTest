A, B = map(int, input().split(" "))
C = int(input())

if 0<=A<=23 and 0<=B<=59 and 0<=C<=1000:
    if B+C >= 60:
        A += int((B+C)/60)
        if A >=24:
            A -= 24
        B = (B+C)%60
    else:
        B += C
print(A, B)