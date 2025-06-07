
# BOJ 11724

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[False] * N for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: x-1, map(int, input().split()))
    adj[a][b] = adj[b][a] = 1
    
#for row in adj:
#    print(row)

ans = 0
chk = [False] * N

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)
    

for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)  # Output the number of connected components
        

