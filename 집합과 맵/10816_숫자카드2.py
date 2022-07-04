# 숫자카드 2(bisect 이용)

from bisect import  bisect_left, bisect_right
from sys import stdin

n = stdin.readline().strip()                            # 상근이가 가지고 있는 카드의 개수
cards = list(map(int, stdin.readline().split()))        # 상근이가 가지고 있는 카드의 리스트
cards.sort()

m = stdin.readline().strip()                            # 비교해야할 카드의 개수
cards_compare = list(map(int, stdin.readline().split()))  # 비교해야할 카드의 리스트


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

for i in range(len(cards_compare)):
    print(count_by_range(cards, cards_compare[i], cards_compare[i]), end=" ")