import sys

input = sys.stdin.readline

sound = list(map(int, input().split()))

if sorted(sound) == sound:
    print("ascending")
elif sorted(sound, reverse=True) == sound:
    print("descending")
else:
    print("mixed")