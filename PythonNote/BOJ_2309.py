from itertools import combinations
import sys

input = sys.stdin.readline

N = 9

height = [int(input()) for _ in range(N)]

for comb in combinations(height,7):
    if sum(comb) == 100:
        for h in sorted(comb):
            print(h)
        break
