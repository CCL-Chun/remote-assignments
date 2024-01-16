def find_position(numbers,target):
  index=0
  for i in numbers:
    if i == target:
      return index
    else:
      index += 1
  return -1
