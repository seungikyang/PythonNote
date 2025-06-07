# BOJ 2178

from platform import machine
import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(n)]

disc = ((0, 1), (1, 0), (0, -1), (-1, 0))  # Right, Down, Left, Up))

def isValidCoord(y, x):
    return 0 <= y < n and 0<= x < m

def bfs():
    chk = [[False] * m for _ in range(n)]
    chk[0][0] = True
    dq = deque()
    dq.append((0,0,1))

    while dq:
        y, x, d = dq.popleft()

        if y == n - 1 and x == m - 1:
            return d

        nd = d + 1
        for dy, dx in disc:
            ny, nx = y + dy, x + dx
            if isValidCoord(ny, nx) and maze[ny][nx] == 1 and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny, nx, nd))

print(bfs())