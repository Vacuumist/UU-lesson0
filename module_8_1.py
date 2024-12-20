def add_everything_up(a, b):
    try:
        result = a + b

#   Это дополнительный блок кода для вывода суммы чисел с плавающей точкой в корректном формате.
#   Число цифр после десятичной точки не может превышать максимальное число цифр в исходных числах.
        decimals = 0
        for i in (a, b):
            if type(i) == float:
                st = str(i)
                decimals = max(len(st[st.find('.')+1:]), decimals)
        result = round(result, decimals)

    except TypeError:
        result = str(a) + str(b)
    return result


print(add_everything_up(123.456, 'строка')) # из-за появления исключения в функции происходит строковое сложение.
print(add_everything_up('яблоко', 4215))

print(add_everything_up(123.456, 7))      # = 130.45600000000002 если нет дополнительного блока кода.
                                                # = 130.456 если в функции есть доподнительный блок кода.

print(add_everything_up(123.23456, 7.43)) # = 130.66456 - в результате 5 цифр после точки, как и в числе а.