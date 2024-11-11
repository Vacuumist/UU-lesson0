def not_email(address):     # Проверка на формат e-mail и домены.
    wrong_address = False
    good_domains = ('.com', '.ru', '.net')
    if '@' not in address or not address.endswith(good_domains):
        wrong_address = True
    return wrong_address

def send_email(message, recipient, *, sender="university.help@gmail.com"):
    recipient = recipient.lower()
    sender = sender.lower()
    if not_email(recipient) or not_email(sender):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', str(recipient) + '.')
    elif sender == recipient:
        print('Невозможно отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', str(recipient) + '.')
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', str(recipient) + '.')

# Tests
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email(sender='University.HELP@gmail.com', recipient='turban.student@mail.ru', message='Доп. тест 1')
send_email('Доп. тест 2', 'University.HELP@Gmail.COM')