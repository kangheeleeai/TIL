# https://www.acmicpc.net/problem/6987
def DFS(home, away):
    global result, tmp
    
    if away == 6:
        home += 1
        away = home+1
    
    if home == 5:
        if result==[[0,0,0] for _ in range(6)]:
            tmp=1
        return

    if result[home][0] > 0 and result[away][2] > 0:
        result[home][0], result[away][2] = result[home][0]-1, result[away][2]-1
        DFS(home, away+1)
        result[home][0], result[away][2] = result[home][0]+1, result[away][2]+1
    
    if result[home][2] > 0 and result[away][0] > 0:
        result[home][2], result[away][0] = result[home][2]-1, result[away][0]-1
        DFS(home, away+1)
        result[home][2], result[away][0] = result[home][2]+1, result[away][0]+1
    
    if result[home][1] and result[away][1] > 0 :
        result[home][1], result[away][1] = result[home][1]-1, result[away][1]-1
        DFS(home, away+1)
        result[home][1], result[away][1] = result[home][1]+1, result[away][1]+1

answer = []
for round in range(4):
    question = list(map(int, input().split())) 
    result = []
    for i in range(6):
        result.append([question[i*3], question[(i*3)+1], question[(i*3)+2] ])
    
    tmp = 0
    DFS(0, 1)
    answer.append(tmp)
    
print(*answer)
