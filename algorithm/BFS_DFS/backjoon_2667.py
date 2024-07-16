# https://www.acmicpc.net/problem/2667

matrix = []
for i in range(row):
    matrix.append(list(map(int, lines[i])))
visited = [[0] * int(row) for _ in range(int(row))]
room_num = 1
room_count = []

def dfs(x, y):
    if x <= -1 or x >= int(row) or y <= -1 or y >= int(row):
        return False
    if matrix[x][y] == 1 and visited[x][y] == 0:
        if len(room_count) < room_num:
          room_count.append(1)
        else:
          room_count[room_num -1] += 1
        visited[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

for i in range(int(row)):
    for j in range(int(row)):
        if visited[i][j] == 1:
          continue
        else:
          if dfs(i, j) == True:
            room_num += 1

room_count.sort()
print(len(room_count))
for i in range(len(room_count)):
    print(room_count[i])
