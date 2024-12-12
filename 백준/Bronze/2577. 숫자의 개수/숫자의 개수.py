import sys

num = 1
for _ in range(3):
    num *= int(sys.stdin.readline().strip())

num = [int(i) for i in str(num)]

for i in range(10):
    print(num.count(i))