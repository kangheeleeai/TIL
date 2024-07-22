# https://www.acmicpc.net/problem/15663

def dfs():
    if len(answer) == M:
        print(" ".join([str(s) for s in answer]))
        return
    remember = 0
    for i in range(N):
        if not visited[i] and remember != nums[i]:
            visited[i] = True
            answer.append(nums[i])
            remember = nums[i]
            dfs()
            visited[i] = False
            answer.pop()

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * N
answer = []

dfs()
