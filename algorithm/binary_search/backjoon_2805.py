# https://www.acmicpc.net/problem/2805

N, M = map(int, input().split())
woods = sorted(list(map(int, input().split())))

def cal_wood_length(cutter):
    length = 0
    for w in woods:
        cut_wood = w-cutter
        if cut_wood < 0:
            cut_wood = 0
        length = length + cut_wood
    return length

def findCutter(start, end, aim):
    if start > end:
        return end
    
    mid = (start + end) // 2
    if cal_wood_length(mid) >= aim:
        return findCutter(mid+1, end, aim)
    else:
        return findCutter(start, mid-1, aim)

print(findCutter(1, max(woods), M))
