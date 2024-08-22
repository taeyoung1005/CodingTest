N, M = map(int, input().split())

decks = {i: 0 for i in range(1, N + 1)}
used_deck_count = 0  # 모든 덱이 한 번씩 사용되었는지 확인하기 위한 카운터

cards = [int(input()) for _ in range(M)]

cnt = 0
for card in cards:
    if decks[card] == 0:  # 새로운 덱이 사용될 때마다 카운터 증가
        used_deck_count += 1
    decks[card] += 1

    cnt += 1
    
    if used_deck_count == N:  # 모든 덱이 한 번씩 사용되었는지 확인
        break
        
if used_deck_count == N:
    print(cnt)
else:
    print(-1)
