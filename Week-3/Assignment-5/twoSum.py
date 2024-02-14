def twoSum(nums, target):
    num_map = {}  # dict to store number and its index
    for index, num in enumerate(nums): # enumerate() return number and its index
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]  # search the complement
        num_map[num] = index  # store index of the current number
    return []  # return an empty list if no solution is found

#test 1
print(twoSum([2, 7, 11, 15], 9))
#test 2
print(twoSum([2, 7, 11, 15], 22))