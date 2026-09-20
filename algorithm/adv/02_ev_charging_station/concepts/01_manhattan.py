"""맨해튼 거리: 가로 이동 거리와 세로 이동 거리를 더한다."""


def manhattan(x1, y1, x2, y2):
    # abs는 차이의 부호를 없앤다. 왼쪽/오른쪽, 위/아래 어느 방향이든
    # 실제로 이동해야 하는 칸 수는 양수이기 때문이다.
    horizontal = abs(x1 - x2)
    vertical = abs(y1 - y2)
    return horizontal + vertical


# 집 A는 (-2, 0)에 있고, 충전소 후보는 (-1, 0)에 있다.
house_x, house_y, allowed = -2, 0, 1
station_x, station_y = -1, 0
distance = manhattan(house_x, house_y, station_x, station_y)

# '허용 거리 이내'이므로 경계에 있는 경우도 만족한다: <= 사용.
print("거리:", distance)  # 1
print("허용 거리 만족:", distance <= allowed)  # True

# 대각선 방향의 두 칸도 거리 1이 아니라 가로 1 + 세로 1 = 2다.
print("대각선 예시:", manhattan(0, 0, 1, 1))  # 2
