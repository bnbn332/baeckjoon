# 문자열 집합

n, m = map(int, input().split())
s = []              # n개의 문자열로 이루어진 집합
for _ in range(n):
    s.append(input())
s.sort()

compare = []        # m개의 문자열로 이루어진 비교해야할 집합
for _ in range(m):
    compare.append(input())

count = 0


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    if binary_search(s, compare[i], 0, n - 1) is not None:
        count += 1

print(count)