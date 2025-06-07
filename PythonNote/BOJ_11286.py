import heapq as hq
import sys

input = sys.stdin.readline

N = int(input())

pq = []

for _ in range(N):
    x = int(input())
    if x:
        hq.heappush(pq, (abs(x), x))
    else:
        print(hq.heappop(pg)[1] if pq else 0)