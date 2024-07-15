# https://www.acmicpc.net/problem/1260

from collections import defaultdict
from collections import deque

tree = defaultdict(list)

N, M, V = map(int, input().split())

for _ in range(M):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

for i in range(N):
    tree[i].sort()

#DFS
stack=[V-1]
visit=list()
while True:
    if not stack:
        break
    node=stack.pop()
    if node not in visit:
        visit.append(node)
        stack.extend(tree[node][::-1])
print(" ".join([str(i+1) for i in visit]))

#BFS
que=deque()
visit=list()
que.append(V-1)

while True:
    if not que:
        break
    node=que.popleft()
    if node not in visit:
        visit.append(node)
        que.extend(tree[node])
print(" ".join([str(i+1) for i in visit]))
