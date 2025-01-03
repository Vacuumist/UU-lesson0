import threading
import time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово №{i+1}\n')
            time.sleep(.1)
    print(f'Завершилась запись в файл {file_name}')

start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end = time.time()
print(f'Работа программы в один поток: {round(end - start, 3)} секунды', end='\n\n')

tread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
tread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
tread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
tread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
start = time.time()
tread_1.start()
tread_2.start()
tread_3.start()
tread_4.start()
tread_1.join()
tread_2.join()
tread_3.join()
tread_4.join()
end = time.time()
print(f'Работа программы в четыре потока: {round(end - start, 3)} секунды')
