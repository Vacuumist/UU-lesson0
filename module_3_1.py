calls = 0

def count_calls():  # A counter for other functions usages
    global calls
    calls += 1

def string_info(string):
    count_calls()
    a = (len(string), string.upper(), string.lower())
    return a

def is_contains(string, list_to_search):
    count_calls()
    result = False
    for i in range(len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            result = True
            break
    return result

print(string_info('Python Developer'))
print(string_info("What's going on in YOUR head?"))
print(string_info('Test_Adress@Gmail.com'))
print(is_contains('Gost', ['ghast', 'ghost', 'GOST', 'guest', 'guess']))
print(is_contains('ТоНар', ['ToHap', 'SHACKMAN', 'Volvo', 'other', 'smth']))
print(is_contains('КТО виноват?', ["Кто виноват?", "Что делать?"]))
print(calls)
