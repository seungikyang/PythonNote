# BOJ 10815
from bisect import bisect_left, bisect_right

import sys
input = sys.stdin.readline

N = int(input())
cards = sorted(map(int, input().split()))

M = int(input())
checks = list(map(int, input().split()))

ans = []

for check in checks:
    left = bisect_left(cards, check)
    right = bisect_right(cards, check)
    ans.append(1 if right > left else 0))

print(*ans)
