# 직각삼각형

while True:
    x, y, z = map(int, input().split())

    if x == 0 and y == 0 and z == 0:
        break

    if x * x == (y * y) + (z * z):
        print("right")
    elif y * y == (x * x) + (z * z):
        print("right")
    elif z * z == (x * x) + (y * y):
        print("right")
    else:
        print("wrong")

