import sys

stack_list = list()
for _ in range(int(input())):
	command = sys.stdin.readline()
	if "push" in command:
		stack_list.append(command.split()[1])
	elif "pop" in command:
		if stack_list:
			pop_element = stack_list.pop()
			print(pop_element)
		else:
			print("-1")
	elif "size" in command:
		print(len(stack_list))
	elif "empty" in command:
		if stack_list:
			print("0")
		else:
			print("1")
	elif "top" in command:
		if stack_list:
			print(stack_list[-1])
		else:
			print("-1")
