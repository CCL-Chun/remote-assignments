# Implement bisect\_left() with python
## request: When there are duplicate numbers in the given input, we usually want to find the first index of the target number. Moreover, when we can’t find the target number, we will return the index which has the smallest number that is larger than the target
```
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 2)) # should print 1 (the index of the target number ‘2’)
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 5)) # should print 2 (the index of the ‘first’ target number ‘5’ shows up)
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 3)) # should print 2 (since it can’t find number 3, return the index of ‘the smallest number larger than 3', that is, the index of the ‘first’ number 5)
```
### Add a if statement in while loop
  - almost the same concept in binary search
  - two pointers to exclude half of candidates and approximate the target
  - check if the target index is the smallest in the number sequence
```
def binary_search_first(numbers, specific):
    if not numbers:
        return "nothing in number list\n"
    target = specific
    length = len(numbers)
    left_p = 0
    right_p = length - 1
    if numbers[left_p] == target:
        return left_p  # first one
    if numbers[right_p] == target:
        return right_p  # last one

    while left_p < right_p: #no need <"=" when check pointers before
        mid_index = left_p + (right_p - left_p) // 2
        mid = numbers[mid_index]
        if target == mid:
            while numbers[mid_index -1] == mid: # mid one and then search left
                mid = numbers[mid_index - 1]
                mid_index -= 1
            return mid_index
        elif target > mid:
            left_p = mid_index + 1  # renew left_p
        else:
            right_p = mid_index - 1  # renew right_p
    return right_p  # not found
```

