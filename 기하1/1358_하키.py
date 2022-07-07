# 하키

import sys
input = sys.stdin.readline

# w = 직사각형 가로 h = 직사각형 세로 x, y = 가장 왼쪽 아래 모서리 p = 선수의 수
w, h, x, y, p = map(int, input().split())

count = 0

for _ in range(p):
    player_x, player_y = map(int, input().split())

    # 직사각형 에 포함되는 경우
    if (x <= player_x <= x + w) and (y <= player_y <= y + h):
        count += 1
        continue
    # 반원에 포함되는 경우
    r = h / 2
    circle_1 = ((player_x - x) ** 2 + (player_y - (y + r)) ** 2) ** 0.5
    circle_2 = ((player_x - (x + w)) ** 2 + (player_y - (y + r)) ** 2) ** 0.5
    if circle_1 <= r or circle_2 <= r:
        count += 1

print(count)