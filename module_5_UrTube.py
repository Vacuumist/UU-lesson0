from time import sleep

class User:
    """Класс пользователя"""
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.hashed_password = hash(password)   # Пароль хранится в зашифрованном виде
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    """Класс видео-ролика"""
    def __init__(self, title, duration, **kwargs):
        self.title = title
        self.duration = duration
        self.time_now = 0
        if 'adult_mode' in kwargs:
            self.adult_mode = kwargs.get('adult_mode')
        else:
            self.adult_mode = False    # Если флаг 18+ не передан при создании видео, по умолчанию ограничений нет.

    def __str__(self):
        return self.title

class UrTube:
    """Класс видео-платформы"""
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        print(self)

    def __str__(self):
        return "<<< Видеоплатформа UrTube >>>"

    def register(self, nickname, password, age):
        for u in self.users:
            if u.nickname == nickname:
                print(f'Пользователь {nickname} уже существует.')
                break
        else:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)

    def log_in(self, nickname, password):
        for u in self.users:
            if u.nickname == nickname and u.hashed_password == hash(password):
                self.current_user = u

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for new_vid in args:
            new = True
            for vid in self.videos:
                if vid.title == new_vid.title:
                    new = False
            if new:
                self.videos.append(new_vid)

    def get_videos(self, request):
        return [v.title for v in self.videos if request.lower() in v.title.lower()]

    def watch_video(self, title):
        if self.current_user is not None:   # Проверка, что пользователь вошёл в аккаунт
            current_video = ''
            for v in self.videos:           # Поиск видео по уникальному названию
                if title == v.title:
                    current_video = v
            if current_video != '':         # Дальше блок кода для найденого видео
                if self.current_user.age >= 18 or not current_video.adult_mode:   # Проверка на 18+ для видео
                    for t in range(current_video.duration + 1):     # Воспроизведение видео начинается с 0 сек.
                        print(t, end=' ')                           # Индикатор воспроизведения видео
                        sleep(1)
                    print('Конец видео.')
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу.')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео.')

# Создание видеоплатформы
ur = UrTube()

# Создание видео
v1 = Video('Лучший язык программирования 2024 года', 15)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)  # Пользователь 18+
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
ur.log_in('vasya_pupkin', 'F8098FM8fjm9jmi')
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

# Воспроизведение видео без ограничения по возрасту пользователем до 18 лет
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Лучший язык программирования 2024 года')