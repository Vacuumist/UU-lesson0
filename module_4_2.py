def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()    # Выводит сообщение из функции inner_function, т.к. она вызывается внутри функции test_function
inner_function()   # Приводит к ошибке, т.к. это имя доступно только внутри функции test_function