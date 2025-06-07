# BOJ 2512

import sys
input = sys.stdin.readline

N = int(input())
money = list(map(int, input().split()))

M = int(input())
maxMoney = max(money)

lo = 0
hi = maxMoney
mid = (lo+hi) //2

ans = 0

def isPossible(mid):
    return sum(min(r, mid) for r in money) <= M


while lo <= hi:
    if isPossible(mid):
        lo = mid + 1
        ans = mid
    else:
        hi = mid - 1

    mid = ( lo + hi ) //2


print(ans)

