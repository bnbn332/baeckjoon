# 숫자카드3(해쉬맵 이용 딕셔너리)

from sys import stdin

n = stdin.readline().strip()
cards = list(map(int, stdin.readline().split()))
m = stdin.readline().strip()
cards_compare = list(map(int, stdin.readline().split()))

hash = {}
print(cards)
for i in cards:     # 키 값이 존재 하면 value가 1씩 늘어나고, 아니면 1
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1


for i in cards_compare:
    if i in hash:
        print(hash[i], end=" ")
    else:
        print(0, end=" ")