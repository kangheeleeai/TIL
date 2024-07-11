# https://www.acmicpc.net/problem/9012

answer=list()
for num in range(int(input())):
	stack=list()
	for i in input():
		if ")" == i:
			if not stack:
				answer.append("NO")
				break
			elif stack[-1]=="(":
				stack.pop()
			else:
				answer.append("NO")
				break
		else:
			stack.append(i)

	if len(answer) != (num+1):
		if not stack:
			answer.append("YES")
		else:
			answer.append("NO")

for p_answer in answer:
	print(p_answer)
