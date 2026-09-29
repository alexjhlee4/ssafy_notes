# SWEA 4012 요리사
# N개 식재료를 N/2개씩 A, B 두 요리로 나눈다
# 요리 맛 = 같은 요리에 들어간 재료 i, j 쌍의 시너지 S[i][j] 합 (S[i][j] != S[j][i])
# 두 요리 맛 차이의 최솟값 구하기
#
# 풀이: 조합 완전탐색
# - 0 ~ N-1 중 N/2개를 고르는 조합을 재귀로 직접 만든다 -> A
# - 나머지 재료 -> B
# - A, B 각각 모든 (i, j) 쌍의 시너지를 더해 차이 비교
# 복잡도: C(N, N/2) * (N/2)^2  (N <= 16 이면 12870 * 64 정도)
# 개선 포인트: A와 B를 뒤집은 경우가 중복 계산됨 -> 0번 재료를 A에 고정하면 절반

import sys

sys.stdin = open('input.txt')

T = int(input())

# 조합의 직접 구현 손으로 따라가 볼 것
def combination(arr, r):
    if r == 0:
        return [[]]

    result = []
    for i in range(len(arr)):
        elem = arr[i]
        next_arr = arr[i + 1 :]

        for rest in combination(next_arr, r-1):
            result.append([elem] + rest)

    return result


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 반으로 나누면 중복 계산을 제거하고 정말 좋겠지만 머리가 따라가지 않는다
    comb = combination(list(range(N)), N//2)

    # 무한대로 초기화
    min_taste_diff = float('inf') 
    for A in comb:
        # A에 포함되지 않는 B리스트를 만든다
        B = [i for i in range(N) if i not in A ]
        
        tmp_A = 0
        tmp_B = 0
        # 한번에 A, B를 모두 처리하기 위해 인덱스를 사용하지만
        # 생각하기 어려우므로 이터 두번 반복하는걸 권장
        
        for i in range(N//2):
            for j in range(N//2):

               if A[i] != A[j]:
                   tmp_A += arr[A[i]][A[j]]
               if B[i] != B[j]:
                   tmp_B += arr[B[i]][B[j]]
        
        tmp_taste_diff = abs(tmp_A - tmp_B)
        if tmp_taste_diff < min_taste_diff:
            min_taste_diff = tmp_taste_diff

    print(f'#{tc} {min_taste_diff}')

        
    