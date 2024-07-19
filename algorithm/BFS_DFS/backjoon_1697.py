# https://www.acmicpc.net/problem/1697

from collections import deque

def bfs(N, K):
    visited = [-1] * 100001 
    visited[N] = 0
    q = deque([N])
 
    while q:
        current_point = q.popleft()
 
        if current_point == K:
            return visited[current_point]
 
        # 이동 경우를 확인 (x+1, x-1, x*2)
        for next_point in (current_point + 1, current_point - 1, current_point * 2):
            if 0 <= next_point <= 100000 and visited[next_point] == -1:
                if next_point == current_point * 2:
                    visited[next_point] = visited[current_point] + 1
                    q.appendleft(next_point)
                else:
                    visited[next_point] = visited[current_point] + 1 # 걸어서 이동은 1초 소요
                    q.append(next_point)

N, K = map(int, input().split())
print(bfs(N, K))
