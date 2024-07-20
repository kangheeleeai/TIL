# https://www.acmicpc.net/problem/14226

from collections import deque

S = int(input())
q = deque()
q.append((1, 0))

visited = dict()
visited[(1, 0)] = 0

while q:
    now, clip = q.popleft()
    if now == S:
        print(visited[(now, clip)])
        break
    if (now, now) not in visited.keys():
        visited[(now, now)] = visited[(now, clip)] + 1
        q.append((now, now))
    if (now+clip, clip) not in visited.keys():
        visited[(now+clip, clip)] = visited[(now, clip)] + 1
        q.append((now+clip, clip))
    if (now-1, clip) not in visited.keys():
        visited[(now-1, clip)] = visited[(now, clip)] + 1
        q.append((now-1, clip))
