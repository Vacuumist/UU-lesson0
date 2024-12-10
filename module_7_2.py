def custom_write(file_name, strings):
    res = dict()
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(len(strings)):
        res.update({(i + 1, file.tell()): strings[i]})
        file.write(f'{strings[i]}\n')
    file.close()
    return res

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)