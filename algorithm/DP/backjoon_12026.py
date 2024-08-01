# https://www.acmicpc.net/problem/12026

N = int(input())
boj_list = list(input())

max_count = float("inf")
dp = [max_count]*N 
dp[N-1] = 0

for i in range(N-1, -1, -1):
    for j in range(i-1, -1, -1):
        if boj_list [i] == "B":
            if boj_list [j] == "J":
                dp[j] = min(dp[j], dp[i] + (i-j)**2)
        elif boj_list [i] == "O":
            if boj_list [j] == "B":
                dp[j] = min(dp[j], dp[i] + (i-j)**2)
        elif boj_list [i] == "J":
            if s[j] == "O":
                dp[j] = min(dp[j], dp[i] + (i-j)**2)

if dp[0] == max_count:
    print(-1)
else:
    print(dp[0])
