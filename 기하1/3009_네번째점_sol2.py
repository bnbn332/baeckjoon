# 네번째 점

x_array = []
y_array = []

for _ in range(3):
    x, y = map(int, input().split())
    x_array.append(x)
    y_array.append(y)

for i in range(3):
    if x_array.count(x_array[i]) == 1:  # x좌표가 한개뿐이면 
        x = x_array[i]
    if y_array.count(y_array[i]) == 1:
        y = y_array[i]

print(x, y)