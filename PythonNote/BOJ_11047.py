import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)
count = 0
tot = 0

for coin in coins:
    if k == 0:
        break
    else:
        if k >= coin:
            count = k//coin
            k -= count * coin
            tot += count

print(tot)