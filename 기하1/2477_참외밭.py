# 참외밭

import sys
input = sys.stdin.readline

# 참외 개수
k = int(input())

# 동 1, 서 2, 남 3, 북 4
height = []
width = []
total = []

for i in range(6):  # 변이 6개
    direction, length = map(int, input().split())
    if direction == 1 or direction == 2:
        width.append(length)
        total.append(length)
    else:
        height.append(length)
        total.append(length)


big_box = max(height) * max(width)

max_height = total.index(max(height))   # total 리스트에서 최대 세로값의 인덱스
print(max_height)
max_width = total.index(max(width))     # total 리스트에서 최대 가로값의 인덱스

# 세로 최대값의 다음값에서 세로 최대값 이전의 가로값을 빼준것이 작은 사각형의 가로값
small_width = abs(total[max_height - 1] - total[(max_height - 5 if max_height == 5 else max_height + 1)])
# 가로 최대값의 다음값에서 가로 최대값 이전의 세로값을 빼준것이 작은 사각형의 세로값
small_height = abs(total[max_width - 1] - total[(max_width - 5 if max_width == 5 else max_width + 1)])

box = big_box - (small_width * small_height)
print("height = ", height)
print("width = ", width)
print("total = ", total)
print(box * k)