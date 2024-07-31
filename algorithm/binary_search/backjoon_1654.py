# https://www.acmicpc.net/problem/1654

N, K = map(int, input().split())
lines = sorted([int(input()) for _ in range(N)])

left = 1 
right = max(lines) 

while left <= right:
    mid = (left+right)//2
    lan_length = 0
    for i in lines:
        lan_length += i//mid
    if lan_length >= K:
        left = mid + 1
    else:
        right = mid - 1 

print(right)
