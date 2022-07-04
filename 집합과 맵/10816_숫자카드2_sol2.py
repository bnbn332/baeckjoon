# 숫자카드2 (counter 이용)

from collections import Counter
from sys import stdin

n = stdin.readline().strip()
cards = list(map(int, stdin.readline().split()))
m = stdin.readline().strip()
cards_compare = list(map(int, stdin.readline().split()))

count = Counter(cards)

for i in range(len(cards_compare)):
    if cards_compare[i] in count:
        print(count[cards_compare[i]], end=" ")
    else:
        print(0, end=" ")