first, second, third = (int(input("Введите первое число: ")),
                        int(input("Введите второе число: ")),
                        int(input("Введите третье число: ")))
if first == second == third:
    print("Одинаковых чисел: 3")
elif first == second or second == third or first == third:
    print("Одинаковых чисел: 2")
else:
    print("Одинаковых чисел: 0")