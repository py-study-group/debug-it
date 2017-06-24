array = [1, 2, 'ham', 3, 'foo', 4, 5]

for element in array:
    if type(element) in (int, float):
        print(element, 'Is digit')
    else:
        print(element, 'Is not digit')
