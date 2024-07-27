#  https://www.acmicpc.net/problem/2661

def check(result, length):
    for i in range(length):
        slice_num = result[i:]
        for j in range(1, len(slice_num)//2+1):
            if slice_num[:j] == slice_num[j:j+j]:
                return False
    return True

def make_sequence(length):
    if not check(result, length):
        return False
    if length == N:
        print(*result, sep="")
        return True
    for i in range(1,4):
        result.append(i)
        if make_sequence(length+1) == 1:
            return True
        result.pop()


N = int(input())
result = list()
make_sequence(0)
