#https://www.acmicpc.net/problem/1012

from collections import deque

#이동용 리스트
dx = [0,0,1,-1]
dy = [1,-1,0,0]


#bfs 함수
def bfs(graph, a, b):
    queue = deque()
    
    #큐에 현재 좌표 입력
    queue.append((a,b))

    #현재 좌표값을 0으로 변경(재반복 방지)
    graph[a][b] = 0
    #큐가 빌때까지 반복
    while queue:
        #큐에서 좌표값 가져오기
        x, y = queue.popleft()

        #이동방향 반복(상하좌우)
        for i in range(4):
            #좌표값 수정
            nx = x+dx[i]
            ny = y+dy[i]

            #종료 조건
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            #해당 좌표값이 1일 경우 작동
            if graph[nx][ny] == 1:
                #해당 좌표값 0으로 변경
                graph[nx][ny] = 0
                #해당 좌표 값을 큐에 입력(다음 좌표로 계속 이동하기 위함)
                queue.append((nx, ny))
    return

t = int(input())

for i in range(t):
    #필요 지렁이 수 카운팅 변수
    cnt = 0
    n, m, k = map(int,input().split())
    #공백 그래프 만들기
    graph = [[0]*m for _ in range(n)]

    # 배추의 위치 입력
    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            #현재 위치에 배추가 있을 경우에만 작동
            if graph[a][b] == 1:
                #bfs호출
                bfs(graph, a, b)
                cnt += 1
    print(cnt)
