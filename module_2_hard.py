number = int(input('Введите число: '))
if number < 3 or number > 20:
    print('Вы ввели некорректное число.')
else:
    result = str()                          # Пустая строковая переменная для записи результата поиска
    for i in range(1, number // 2 + 1):     # Для меньшего числа в паре нужно проверить только половину значений
        for j in range(i + 1, number):      # Большее число в паре не превышает введённого числа
            if number % (i + j) == 0:       # Проверка кратности введённого числа сумме проверяемых чисел
                result += str(i) + str(j)   # Добавление найденной пары чисел к строке с паролем
    print('Пароль: ', result)
