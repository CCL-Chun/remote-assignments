# Algorithm Practice
  - find two numbers add up to the given target
* first though: use nested loop to sum the two numbers
```
def twoSum(nums, target):
    n1 = 0 #for counting
    for num_1 in nums:
        n2 = n1 + 1 #count the next number
        for num_2 in nums[n2:]:
            total = num_1 + num_2
            if total == target:
                answer = [n1,n2]
                return answer
            n2 += 1
```
* time complexity $\(O(n^2)\)$
## Better way
  - use hash table (dict in python) to store the number and its index
  - search the complement for the target or save them into dict if not found
```
def twoSum(nums, target):
    num_map = {}  # dict to store number and its index
    for index, num in enumerate(nums): # enumerate() return number and its index
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]  # search the complement
        num_map[num] = index  # store index of the current number
    return []  # return an empty list if no solution is found
```
* time complexity $\(O(n)\)$
* only walk through the number sequence one time and check if the complement had been saved in dict
