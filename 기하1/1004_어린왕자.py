# 어린왕자

import sys
input = sys.stdin.readline

# T = 테스트 케이스 개수
t = int(input())

for _ in range(t):
    # 출발점(x1, y1), 도착점(x2, y2)
    x1, y1, x2, y2 = map(int, input().split())
    # 행성계의 개수 n
    n = int(input())
    count = 0   # 진입 이탈 횟수
    for _ in range(n):
        # 행성계 중점(cx, cy) 반지름(r)
        cx, cy, r = map(int, input().split())
        # 행성 줌심부터 시작점 까지의 거리
        start = (((x1 - cx) ** 2) + ((y1 - cy) ** 2)) ** 0.5
        end = (((x2 - cx) ** 2) + ((y2 - cy) ** 2)) ** 0.5

        # 시작점 또는 도착점이 중심 사이의 거리보다 작다면 count +1
        if start < r or end < r:
            # 시작점 또는 도착점 모두 포함된다면 pass
            if start < r and end < r:
                pass
            else: count += 1

    print(count)