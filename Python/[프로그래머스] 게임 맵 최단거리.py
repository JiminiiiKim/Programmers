# 상하좌우 모두 살피고 누적합으로 visit 역할 대신 함.

from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(maps, x, y, n, m) :
    queue = deque()
    queue.append((x, y))

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m : # 칸 초과
                continue
            elif maps[nx][ny] == 0 : # 막혀있는 길
                continue
            elif maps[nx][ny] == 1 : # 새로운 길
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    return maps[n-1][m-1]

def solution(maps) :
    n, m = len(maps), len(maps[0])
    answer = bfs(maps, 0, 0, n, m)
    if answer == 1 :
        return -1
    else :
        return answer