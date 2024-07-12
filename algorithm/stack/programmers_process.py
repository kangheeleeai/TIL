# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
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

    answer = int(print_list.index(location)) + 1
    
    return answer
