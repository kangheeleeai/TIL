# https://www.acmicpc.net/problem/15651

def dfs():
    if len(answer) == M:
        print(" ".join([str(s) for s in answer]))
        return
    for i in range(N):
        answer.append(nums[i])
        dfs()
        answer.pop()

N, M = map(int, input().split())
nums = list(range(1, N+1))
answer = []

dfs()
