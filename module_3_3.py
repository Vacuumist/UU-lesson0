def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(False, "is", "'Not True'")
print_params(4, 'plus 2 =', c=42)
print_params([4, 'plus 2 =', 42], False)
print_params(b=25)
print_params(c = [1,2,3])

values_list = ['This is', 42, False]
values_dict = {'a': 532, 'b': 'test string', 'c': 3.14}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3.14, 'equal to']
print_params(*values_list_2, 42)