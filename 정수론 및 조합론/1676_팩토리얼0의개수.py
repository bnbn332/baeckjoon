# 팩토리얼 0의 개수 str로 바꿔서 뒤집은 뒤 0이 끝날때까지 개수를 셈

from math import factorial

n = int(input())
count = 0

for x in str(factorial(n))[::-1]:
    if x != '0':
        break
    count += 1
print(count)