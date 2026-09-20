"""완전탐색: 격자의 후보를 모두 만들고, 서로 다른 두 칸을 선택한다."""

from itertools import combinations


# 실제 문제에서는 range(-15, 16)을 쓴다. range의 끝값 16은 포함되지 않는다.
# 여기서는 출력이 짧도록 -1부터 1까지의 작은 격자로 연습한다.
coordinates = range(-1, 2)
occupied = {(0, 0), (1, 1)}  # 집이 있는 칸에는 충전소를 지을 수 없다.
spots = []

for x in coordinates:
    for y in coordinates:
        if (x, y) in occupied:
            continue
        spots.append((x, y))

print("건설 가능한 칸:", spots)
print("후보 수:", len(spots))  # 3 x 3 - 집이 있는 2칸 = 7

# combinations(spots, 2)는 두 칸을 한 번씩만 선택한다.
# (A, B)를 확인했다면 (B, A)는 다시 확인하지 않는다.
pairs = list(combinations(spots, 2))
print("두 칸을 고르는 방법의 수:", len(pairs))  # 7 * 6 / 2 = 21
print("첫 번째 조합:", pairs[0])
