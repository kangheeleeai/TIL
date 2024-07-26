l, c = map(int, input().split())
words = sorted(list(map(str, input().split())))
answer = []

def make_word(cnt, idx):
    if cnt == l:
        vo, co = 0, 0

        for i in range(l):
            if answer[i] in ['a', 'e', 'i', 'o', 'u']:
                vo += 1
            else:
                co += 1

        if vo >= 1 and co >= 2:
            print("".join(answer))

        return

    for i in range(idx, c):
        answer.append(words[i])
        make_word(cnt + 1, i + 1)
        answer.pop()

make_word(0, 0)
