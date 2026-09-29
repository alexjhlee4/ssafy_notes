# SWEA 5189 전자카트
# 사무실(0번)에서 출발해 모든 관리구역을 한 번씩 방문하고 사무실로 돌아온다
# arr[i][j] = i -> j 이동 시 배터리 사용량 (방향마다 다름)
# 배터리 사용량 최솟값 구하기
#
# 풀이: 순열 완전탐색
# - 출발점 0은 고정, 1 ~ N-1 의 방문 순서를 순열로 전부 만든다
# - 경로 비용 = 순서대로 이동 비용 합 + 마지막 구역 -> 0 복귀 비용
# 복잡도: (N-1)! * N  (N <= 10 이면 약 360만 번)
# 개선 포인트: 순열을 다 만든 뒤 계산하지 말고 재귀 중에 비용을 누적하면서
#             현재 비용 >= min 이면 가지치기 (백트래킹)

import sys

sys.stdin = open('input.txt')

T = int(input())

def perm(selected, remaining):
    if not remaining:
        res.append(selected)
        return

    for i in range(len(remaining)):
        pick = remaining[i]
        next_remaining = remaining[:i] + remaining[i+1:]
        perm(selected + [pick], next_remaining)



for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = []
    perm([0] , list(range(1,N)))
    
    min_con = float('inf')
    for per in res:
        tmp = 0
        for i in range(len(per)):
            if i < len(per) - 1:
                tmp += arr[per[i]][per[i+1]]
            else:
                tmp += arr[per[i]][0]
        if tmp < min_con:
            min_con = tmp
    print(f"#{tc} {min_con}")