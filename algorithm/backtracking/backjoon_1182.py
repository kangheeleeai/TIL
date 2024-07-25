N, S = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
answer = []


def subsequence(start):
    global cnt
    if sum(answer) == S and len(answer) > 0:
        cnt += 1

    for i in range(start, N):
        answer.append(num[i])
        subsequence(i+1)
        answer.pop()


subsequence(0)
print(cnt)
