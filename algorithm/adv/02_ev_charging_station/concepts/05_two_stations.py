"""충전소 1개가 불가능할 때, 2개 조합의 커버 여부와 거리 합을 확인한다."""

from itertools import combinations


houses = [(-2, 0, 1), (1, 3, 2)]
occupied = {(x, y) for x, y, _ in houses}
spots = []
full = (1 << len(houses)) - 1

for station_x in range(-15, 16):
    for station_y in range(-15, 16):
        if (station_x, station_y) in occupied:
            continue

        distances = []
        mask = 0
        for index, (house_x, house_y, allowed) in enumerate(houses):
            distance = abs(station_x - house_x) + abs(station_y - house_y)
            distances.append(distance)
            if distance <= allowed:
                mask |= 1 << index

        # 어떤 집도 담지 못하는 자리는 2개 조합에 필요하지 않다.
        # 1개로 모든 집을 담는 자리가 없다면, 두 자리 모두 적어도 한 집은 담아야 한다.
        if mask:
            spots.append(((station_x, station_y), mask, distances))

# 반드시 1개짜리 답을 먼저 찾는다. 있으면 2개 탐색을 하지 않는다.
one_station_costs = [sum(distances) for _, mask, distances in spots if mask == full]

if one_station_costs:
    answer = min(one_station_costs)
else:
    answer = None
    for (_, mask_a, distances_a), (_, mask_b, distances_b) in combinations(spots, 2):
        # 두 충전소 중 어느 쪽도 허용 거리 안에 없는 집이 있다면 탈락한다.
        if (mask_a | mask_b) != full:
            continue

        # 각 집은 두 충전소 중 더 가까운 곳을 사용한다.
        # 허용 거리 확인에는 비트마스크를, 거리 합 계산에는 실제 거리를 쓴다.
        total = sum(min(a, b) for a, b in zip(distances_a, distances_b))
        if answer is None or total < answer:
            answer = total

    # 가능한 조합을 끝까지 찾지 못하면 문제에서 요구한 -1을 출력한다.
    if answer is None:
        answer = -1

print("최소 거리 합:", answer)  # 2
