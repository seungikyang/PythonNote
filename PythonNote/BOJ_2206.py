# BOJ 2206

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

def bfs() -> int:
    global visited, directions
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    while q:
        x, y, broken = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][broken]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0<= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    q.append((nx, ny, broken))
                elif grid[nx][ny] == 1 and visited[nx][ny][broken] == 0:
                    if broken == 0:
                        visited[nx][ny][1] = visited[x][y][broken] + 1
                        q.append((nx, ny, 1))
                    elif broken == 1:
                        continue
    return -1


def solution(n, m, grid) -> int:
    global visited, directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    answer = bfs()
    return answer

print(solution(n, m, grid))
