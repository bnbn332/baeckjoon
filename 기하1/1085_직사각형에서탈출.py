# 직사각형에서 탈출

# 현재위치 (x,y) 왼쪽 아래 (0,0) 오른쪽 위 (w,h) 직사각형 경계선까지 가는 거리의 최솟값

x, y, w, h = map(int, input().split())

print(min(x, y, (w - x), (h - y)))