
#BOJ 10844: 쉬운 계단 수
MOD = 1_000_000_000

from re import A
import sys
input = sys.stdin.readline

#cache[n][d] = n자리 수 중 끝자리가 d인 쉬운 계단 수의 개수

cache = [[0] * 10 for _ in range(101)]
for j in range(1, 10):
    cache[1][j] = 1  # 1자리 수는 각 숫자마다 하나씩
    
for i in range(2, 101):
    for j in range(10):
        if j > 0:
            cache[i][j] += cache[i-1][j-1]
            cache[i][j] %= MOD
        if j < 9:
            cache[i][j] += cache[i-1][j+1]
            cache[i][j] %= MOD

N = int(input().strip())

ans = 0
for j in range(10):
    ans += cache[N][j]
    ans %= MOD

print(ans)  # N자리 쉬운 계단 수의 개수 출력
