
# BOJ 11051: 이항 계수 2
import sys
input = sys.stdin.readline

MOD = 10007

N, K = map(int, input().split())

cache = [[0] * (N + 1) for _ in range(N+1)]]


def bino(n, k):
    if cache[n][k]:
        return cache[n][k]

    if k == 0 or k == n:
        cache[n][k] = 1
    else:
        cache[n][k] = bino(n-1, k-1) + bino(n-1,k)

    return cache[n][k]


print(bino(N,K) % MOD)