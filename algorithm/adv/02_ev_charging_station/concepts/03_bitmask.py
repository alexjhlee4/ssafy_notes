"""비트마스크: 한 좌표가 허용 거리 안에 담는 집을 정수 하나로 표현한다."""


houses = [
    (0, 0, 1),  # 0번 집: 좌표 x, y와 허용 거리 d
    (2, 0, 1),  # 1번 집
    (4, 0, 1),  # 2번 집
]


def coverage_mask(station_x, station_y):
    mask = 0  # 처음에는 아무 집도 커버하지 않는다: 이진수 000
    for index, (house_x, house_y, allowed) in enumerate(houses):
        distance = abs(station_x - house_x) + abs(station_y - house_y)
        if distance <= allowed:
            # 1 << index는 index번째 자리만 1인 숫자다.
            # | 연산은 기존 비트를 유지하면서 해당 집의 비트를 켠다.
            mask |= 1 << index
    return mask


left = coverage_mask(1, 0)  # 0번과 1번 집을 커버: 011
right = coverage_mask(3, 0)  # 1번과 2번 집을 커버: 110
full = (1 << len(houses)) - 1  # 모든 집을 커버한 상태: 111

print("왼쪽 후보:", format(left, "03b"))
print("오른쪽 후보:", format(right, "03b"))
print("1개로 모두 커버:", left == full)  # False
print("2개로 모두 커버:", (left | right) == full)  # True

# 첫 후보가 못 담은 집(need)을 두 번째 후보가 모두 담는지 확인해도 된다.
need = full & ~left
print("두 번째 후보가 반드시 담아야 할 집:", format(need, "03b"))
print("남은 집을 모두 담는가:", (right & need) == need)  # True
