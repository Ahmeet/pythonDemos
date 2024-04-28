from operator import itemgetter

elements = [1, 2, 3, 4, 5]

selectedElements = itemgetter(0, -1)

print(selectedElements(elements))

#######################################


items = {'a': 1, 'b': 2, 'c': 3}

selectedValues = itemgetter('a', 'c')

print(selectedValues(items))
