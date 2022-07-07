# 터렛

import math

t = int(input())

for _ in range(t):
    # 조규현의 좌표(x1, y1), 백승환의 좌표(x2, y2), 조규현-류재명 거리 r1, 백승환-류재명 거리 r2
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두원의 거리
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if distance == 0 and r1 == r2:   # 두 원이 동심원이고 반지름이 같을 때
        print(-1)
    elif abs(r1 - r2) == distance or r1 + r2 == distance:    # 내접 또는 외접일때
        print(1)
    elif abs(r1 - r2) < distance < r1 + r2:  # 두 원이 서로다른 두점에서 만날 때
         print(2)
    else:
        print(0)