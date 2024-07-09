#https://www.acmicpc.net/problem/1158

inputs = input().split()
jump_num = int(inputs[1]) 
nums = list(range(1, int(inputs[0])+1))

remove_idx = jump_num - 1
answer = list()

while len(nums):
	if remove_idx >= len(nums):
		remove_idx = remove_idx - len(nums)
	else: 
		answer.append(str(nums[remove_idx]))
		nums.pop(remove_idx)
		remove_idx += (jump_num-1)
		
print("<"+", ".join(answer)+">")
