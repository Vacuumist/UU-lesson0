from datetime import datetime
from multiprocessing import Pool
from multiprocessing import Process


def read_info(file_name):
    all_data = [1]
    s = 1
    with open(file_name, 'r') as file:       # открытие файла для чтения
        while s:                             # цикл чтения закончится при получении пустой строки из файла
            s = file.readline().strip('\n')  # чтение строки с удалением считанных переносов на следующую строку
            all_data.append(s)               # добавление ститанной строки в список
        all_data.pop()                       # удаление пустой строки (последнего элемента списка)


filenames = [f'./file {number}.txt' for number in range(1, 5)]   # создание списка имён файлов

if __name__ == '__main__':      # Все варианты вызова функции помещены в if __name__ == '__main__'
                                # для возможности корректного вывода в консоль всех результатов за один запуск модуля
# Линейный вызов:
    start_time = datetime.now()
    [read_info(file) for file in filenames]
    end_time = datetime.now()
    print('Линейный вызов:              ', end_time - start_time)

# Многопроцессый вызов с применением Pool:
    for i in range(1, 5):                  # цикл добавлен для запуска вариантов от одного до четырёх процессов
        start_time = datetime.now()
        with Pool(i) as pool:              # Конструкция c with добавлена в соотвествии с условием задачи, но в данном
            pool.map(read_info, filenames) # случае можно было ограничиться строкой Pool(i).map(read_info, filenames)
        end_time = datetime.now()
        print(f'{i}-хпроцессый вызов (Pool):   ', end_time - start_time)

# Многопроцессый вызов без применения Pool и списка файлов:
    start_time = datetime.now()
    processes = [Process(target=read_info, args=('file '+str(i)+'.txt',)) for i in range(1, 5)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    end_time = datetime.now()
    print('4-xпроцессый вызов (Process):', end_time - start_time)