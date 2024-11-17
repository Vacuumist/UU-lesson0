# Recursive multiplication
def get_multiplied_digits(number):
    while number % 10 == 0 and number != 0:
        number = int(number / 10)
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

print(get_multiplied_digits(40203))     # = 24
print(get_multiplied_digits(4020300))   # = 24
print(get_multiplied_digits(0))         # = 0