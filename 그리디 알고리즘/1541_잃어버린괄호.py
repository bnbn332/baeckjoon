# 잃어버린 괄호
# 최초로 마이너스가 나오기전 까지 모두 더하고 마이너스가 나오는 순간 그 뒤에 있는 수를 모두 빼준다

import sys
input = sys.stdin.readline

arr = input().split("-")
s = 0

for i in arr[0].split("+"):
    s += int(i)

for i in arr[1:]:
    for j in i.split("+"):
        s -= int(j)

print(s)