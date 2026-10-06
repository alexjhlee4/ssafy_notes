import sys

# M이 주어지지 않았으므로 , M이 몇인지 알아내서 불리언 배열로 관리해서
# 몬스터[M] 을 다녀 오지 않았으면 커스터머[M]에 들어가지 못하게
# 근데 커스터머 M은 필요한가? 필요하지 모두가 찍히는 순간이 최솟값이니까
# 그럼 와일문을 q or False not in 커스터머 배열 
# 그리고 끝나는 순간에 마지막에 들어온 커스터머에 이동 횟수를 꺼내 가져온다
# q에서 마지막에 오른쪽에서 팝하면 되지 않을까?
# 이게 아닌가? M 을 구하고 모두 순열을 짜서 거기 맨해튼 거리를 구해서 최소값 고쳐나가야하나
# 순열을 짜서 bfs로 각 순열들의 최소거리만큼씩 가고 그걸 계속 더한 값들의 최솟값??
# 이게 최선인가? 


# M의 수를 찾아 주는 함수 4까지여서 하드 코딩함
def find_M(arr):
    for i in [4,3,2,1]:
        for row in arr:
            if i in row:
                return i

#  순열 백본에서 조합을 만들 수 있지 않을까  
# 리메이닝에는 뭐가 들어와야 할 것인가 1, -1, 2, -2, 3, -3 넣자
# 프루닝 하며 순열을 짠다 ex: 1이 들어와야 -1 이 들어갈 수 있음
def make_orders(selected: list , remaining, orders):
    if not remaining:
        orders.append(selected)
        return

    for i in range(len(remaining)):
        
        # 해당 몬스터를 아직 안 잡았으면 그 고객은 지금 못 뽑는다
        if remaining[i] < 0 and abs(remaining[i]) not in selected:
            continue
        make_orders(selected+[remaining[i]], remaining[:i] + remaining[i+1:], orders)

# 아이템의 좌표를 찾아주는 함수 
# N 이 썩 크지는 않지만 여러번 쓰지 않게 주의
def find_coordinates(target: int):
    for r in range(N):
        for c in range(N):
            if target == arr[r][c]:
                return r, c

sys.stdin = open('input.txt')

T = int(input())



for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    M = find_M(arr)

    
    targets = []
    for i in range(1, M + 1):
        targets.append(i)
        targets.append(-i)

    # 타겟과 타겟의 좌표를 키밸류로 담을 딕셔너리
    coords = {}
    for target in targets:
        coords[target] = find_coordinates(target)

    # 오더들을 담을 리스트
    orders = []
    make_orders([], targets, orders)

    min_dist = float('inf')

    for order in orders:
        dist = 0
        for i in range(2 * M):
            if i == 0:
                r, c = coords[order[i]]
                dist += (r + c)
            else:
                prev_r, prev_c = r, c
                r, c = coords[order[i]]
                dist += (abs(r-prev_r) + abs(c-prev_c))
        if min_dist > dist:
            min_dist = dist

    print(f'#{tc} {min_dist}')
        






