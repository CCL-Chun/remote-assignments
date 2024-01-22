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

# test target in numbers
print(binary_search_first([1,2,5,5,5,6,7],5))
# test target not in numbers
print(binary_search_first([1,2,5,5,5,6,7],3))