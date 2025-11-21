import sys

n = sys.stdin.readline()
a = set(sys.stdin.readline().split())
m = sys.stdin.readline()
result = ['1' if i in a else '0' for i in sys.stdin.readline().split()]

print("\n".join(result))
