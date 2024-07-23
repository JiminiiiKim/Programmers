from collections import deque

def bfs(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n, m = len(board), len(board[0])
    
    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 'R' :
                start_x, start_y = i, j
                
    # 응용 포인트1: (좌표x, 좌표y, [경로])
    visited = [[float("inf")]*m for _ in range(n)]
    queue = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = 0

    while queue :
        x, y, d = queue.popleft()

        # 응용 포인트2: 문제에서 제시하는 종료 조건
        if board[x][y] == 'G' : 
            return d

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'D' :
                nx += dx[i]
                ny += dy[i]
            nx -= dx[i]
            ny -= dy[i]
            if visited[nx][ny] > d+1 :
                visited[nx][ny] = d+1
                queue.append((nx, ny, d+1))

    return -1

def solution(board):
    answer = 0
                
    answer = bfs(board) 
    
    return answer