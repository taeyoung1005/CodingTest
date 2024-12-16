import sys

input = sys.stdin.readline

N = int(input())
cards_dict = {}
cards = list(map(int, input().split()))

for card in cards:
    if card in cards_dict:
        cards_dict[card] += 1
    else:
        cards_dict[card] = 1

M = int(input())
print(" ".join([str(cards_dict[i]) if i in cards_dict else '0' for i in list(map(int, input().split()))]))