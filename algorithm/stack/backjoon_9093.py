# https://www.acmicpc.net/problem/9093

answer = list()

for _ in range(int(input())):
    input_str = input()
    word_reverse = [word[::-1] for word in input_str.split()]
    answer.append(" ".join(word_reverse))
for print_answer in answer:
	print(print_answer)
