"""충전소 개수 최소화: 1개로 가능하면 그중 거리 합이 최소인 자리만 고른다."""


houses = [(-2, 0, 3), (0, 0, 3), (2, 0, 3)]
occupied = {(x, y) for x, y, _ in houses}
best = None  # 아직 가능한 충전소 위치를 찾지 못했다는 뜻
best_spot = None

# 실제 문제의 전체 범위에서 건설 가능한 한 칸씩 확인한다.
for station_x in range(-15, 16):
    for station_y in range(-15, 16):
        if (station_x, station_y) in occupied:
            continue

        distances = [
            abs(station_x - house_x) + abs(station_y - house_y)
            for house_x, house_y, _ in houses
        ]

        # 하나라도 허용 거리를 넘으면 이 자리에는 1개만 지을 수 없다.
        if any(distance > house[2] for distance, house in zip(distances, houses)):
            continue

        total = sum(distances)
        if best is None or total < best:
            best = total
            best_spot = (station_x, station_y)

# 이 예시는 1개로 가능하다. 따라서 2개를 지으면 거리 합이 줄어들더라도
# 문제의 '가능한 최소 개수' 규칙에 따라 여기서 답을 확정한다.
print("1개 충전소의 최소 거리 합:", best)  # 5
print("선택한 위치:", best_spot)  # (-1, 0) 또는 (1, 0)
