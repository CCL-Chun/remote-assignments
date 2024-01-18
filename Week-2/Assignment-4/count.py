"""counting input element amount"""
def count(objects):
    """get input objects"""
    listed = {}
    for element in objects:
        if element not in listed:
            listed[element] = 1
        else:
            listed[element] += 1
    return listed

print(count(['x', 'b', 'c', 'a', 'j', 'a', 'x'])) #test
