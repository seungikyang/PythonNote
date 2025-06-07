import sys
input = sys.stdin.readline

N = int(input())

d = dict()

for _ in range(N):
    book = input().strip()
    if book in d:
        d[book] += 1
    else:
        d[book] = 1

m = max(d.values())

result = []

for key, value in d.items():
    if value == m:
        result.append(key)

print(sorted(result)[0])
