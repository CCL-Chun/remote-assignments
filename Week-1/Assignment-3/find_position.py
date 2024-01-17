def find_position(numbers, target):
    if not numbers:
        return "please enter at least 1 number"
    index = 0
    for i in numbers:
        if i == target:
            return index
        else:
            index += 1
    return -1
