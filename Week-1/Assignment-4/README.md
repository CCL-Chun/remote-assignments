# Implement binary search with python
  - requirement
```
print(binary_search_position([1, 2, 5, 6, 7], 1)) # should print 0 
print(binary_search_position([1, 2, 5, 6, 7], 6)) # should print 3
```
## first create a left pointer and a right pointer
  - left one points to the first index (0)
  - right one points to the last index (length -1)
```
def binary_search_position(numbers, specific):
    if not numbers:
        return "nothing in number list\n"
    target = specific
    length = len(numbers)
    left_p = 0
    right_p = length - 1

    # check if the target is the first or the last target
    if numbers[left_p] == target:
        return left_p  # first one
    if numbers[right_p] == target:
        return right_p  # last one
```
## use while loop to approximate the target
  - set the middle index as left\_p + (right\_p - left\_p) // 2
  - refresh the left pointer index to middle index when the target is larger than the middle; vice versa
  - if find no target number, return -1
```
while left_p <= right_p:
    mid_index = left_p + (right_p - left_p) // 2
    mid = numbers[mid_index]
    if target == mid:
        return mid_index  # mid one
    elif target > mid:
        left_p = mid_index + 1  # renew left_p
    else:
        right_p = mid_index - 1  # renew right_p
return -1  # not found
``` 
