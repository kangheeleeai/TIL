#https://www.acmicpc.net/problem/1966

answer = list()

for _ in range(int(input())):
    N, M = map(int, input().split())
    priorities = input().split()

    num_list = list(range(len(priorities)))
    print_list = list()
    while len(priorities):
        max_prioritiy = max(priorities)
        if priorities[0] == max_prioritiy:
            print_list.append(num_list[0])
            num_list.pop(0)
            priorities.pop(0)
        else:
            num_list.append(num_list[0])
            num_list.pop(0)
            priorities.append(priorities[0])
            priorities.pop(0)

    answer.append(int(print_list.index(M)) + 1)

for i in answer:
    print(i)
