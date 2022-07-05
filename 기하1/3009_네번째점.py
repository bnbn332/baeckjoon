# 네번째 점

first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))

if first[0] == second[0]:
    x = third[0]
elif first[0] == third[0]:
    x = second[0]
else:
    x = first[0]

if first[1] == second[1]:
    y = third[1]
elif first[1] == third[1]:
    y = second[1]
else:
    y = first[1]

print(x, y)