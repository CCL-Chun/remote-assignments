def find_max(numbers):
    if not numbers:
        return "please give at least a number"
    max_number=numbers[0]
    for i in numbers:
        if i > max_number:
            max_number=i
    return max_number
