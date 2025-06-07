
# BOJ 2748: 피보나치 수 2
import sys
input = sys.stdin.readline

cache = [-1] * 91
cache[0] = 0
cache[1] = 1

def f(n):
    if cache[n] == -1:
        cache[n] = f(n-1) + f(n-2)
    return cache[n]


print(f(int(input().strip())))