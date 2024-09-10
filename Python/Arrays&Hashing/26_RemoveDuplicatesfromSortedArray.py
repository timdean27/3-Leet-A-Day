def removeDuplicates(nums):
	j = 0
	for i in range(1, len(nums)):
		print(i,j)
		if nums[j] != nums[i]:
			j += 1
			nums[j] = nums[i]
			print(nums)
	return j + 1

print(removeDuplicates([1,1,2,3,4,5,6,7,7,7,7]))