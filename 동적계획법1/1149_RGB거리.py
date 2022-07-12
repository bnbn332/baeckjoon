# RGB 거리

# n번 집 색과 n - 1번 집 색이 같지 않아야 한다.

import sys
input = sys.stdin.readline

# 집의 수 N, 빨, 초, 파 비용
n = int(input())

rgb = []
for _ in range(n):
    rgb.append(list(map(int, input().split())))

for i in range(1, n):
    # 현재 집이 빨간색 이면 이전 집이 초록 또는 파랑 중 더 작은 비용
    rgb[i][0] = min(rgb[i - 1][1], rgb[i - 1][2]) + rgb[i][0]
    # 현재 집이 초록색 이면 이전 집이 빨강 또는 파랑 중 더 작은 비용
    rgb[i][1] = min(rgb[i - 1][0], rgb[i - 1][2]) + rgb[i][1]
    # 현재 집이 파란색 이면 이전 집이 빨강 또는 초록 중 더 작은 비용
    rgb[i][2] = min(rgb[i - 1][0], rgb[i - 1][1]) + rgb[i][2]

print(min(rgb[n - 1][0], rgb[n - 1][1], rgb[n - 1][2]))
