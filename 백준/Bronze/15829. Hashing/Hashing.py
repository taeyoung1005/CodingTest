import sys

input = sys.stdin.readline

alpha =  {value:idx+1 for idx, value in enumerate("abcdefghijklmnopqrstuvwxyz")}

N = int(input().strip())
r = 31
M = 1234567891

result = 0
s = input().strip()
for i in range(len(s)):
    result += alpha[s[i]] * r**i

print(result % M)