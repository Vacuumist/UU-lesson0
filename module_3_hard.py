# Рекурсивная функция, подсчитывающая сумму чисел и длин строк с раскрытием списков, кортежей, множеств и словарей.
def summator(arg):
    sum_ = 0
    for i in range(len(arg)):
        if isinstance(arg[i], int) or isinstance(arg[i], float):
            sum_ += arg[i]           # числа - элементы коллекций просто суммируются
        elif isinstance(arg[i], str):
            sum_ += len(arg[i])      # суммируются длины строк
        elif isinstance(arg[i], list) or isinstance(arg[i], tuple):
            sum_ += summator(arg[i]) # элементы списка или кортежа обрабатываются вызовом этой же фукции
        elif isinstance(arg[i], dict):
            sum_ += summator(list(arg[i].items()))  # словарь преобразуется и обрабатывается как список
        elif isinstance(arg[i], set):
            sum_ += summator(list(arg[i]))  # множество преобразуется и обрабатывается как список
    return sum_

data_structure = [                  # исходные данные задачи
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(summator(data_structure))     # вызов рекурсивной функции
