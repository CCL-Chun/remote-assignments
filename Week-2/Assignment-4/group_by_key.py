""" return an object which shows the summed up value of each key"""
def group_by_key(input2):
    """ return an object which shows the summed up value of each key"""
    pre = {}
    for elements in input2:
        details = list(elements.values())
        if details[0] not in pre:
            pre[details[0]] = details[1]
        else:
            pre[details[0]] = pre[details[0]] + details[1]
    return pre

print(group_by_key(input2 = [{'key': 'a', 'value': 3}, {'key': 'b', 'value': 1},
                             {'key': 'c', 'value': 2}, {'key': 'a', 'value': 3},
                             {'key': 'c', 'value': 5}]))
