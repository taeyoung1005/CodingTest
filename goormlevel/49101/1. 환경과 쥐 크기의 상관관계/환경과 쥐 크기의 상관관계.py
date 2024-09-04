N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A와 B 리스트에서 숫자 빈도를 계산하여 딕셔너리로 저장
A_count = {i: 0 for i in set(A)}  # set으로 중복을 제거한 후 딕셔너리 생성
B_count = {j: 0 for j in set(B)}

# 빈도 계산
for i in A:
    A_count[i] += 1
for j in B:
    B_count[j] += 1

A_max = 0
B_max = 0
A_repr = 0
B_repr = 0

# 최대 값 찾기
max_val = max(max(A_count.keys()), max(B_count.keys()))

# 슬라이딩 윈도우로 범위 내 값들을 빠르게 합산
for i in range(1, max_val + 1):
    # i-2 <= x <= i+2에 해당하는 값만 추출하여 합산
    A_temp = sum(A_count[x] for x in range(i-2, i+3) if x in A_count)
    B_temp = sum(B_count[x] for x in range(i-2, i+3) if x in B_count)
    
    if A_temp > A_max:
        A_max = A_temp
        A_repr = i
    
    if B_temp > B_max:
        B_max = B_temp
        B_repr = i

# 결과 출력
print(f'{A_repr} {B_repr}')
print('good' if A_repr > B_repr else 'bad')
