grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)    # Преобразование множества в список для возможности сортировки
students.sort()              # Сортировка списка имён по алфавиту
avg_grades = {students[0]: sum(grades[0]) / len(grades[0]),  # Создание словаря из имён студентов и средних оценок
              students[1]: sum(grades[1]) / len(grades[1]),  # Словарь создан поэлементно, т.к. циклы ещё не проходили.
              students[2]: sum(grades[2]) / len(grades[2]),
              students[3]: sum(grades[3]) / len(grades[3]),
              students[4]: sum(grades[4]) / len(grades[4])}
print(avg_grades)                                            # Вывод полученного словаря на экран
