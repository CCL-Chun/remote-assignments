def binary_search_position(numbers, specific):
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
