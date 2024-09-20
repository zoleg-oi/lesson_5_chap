# Свой YouTube
import time


class User:
    '''
    Класс принимает параметры
    nickname тип строка (имя пользователя)
    password тип число (пароль)
    age тип число (возраст)
    реализует атрибуты
    "nickname"
    с проверкой на тип строка
    "password"
    содержит хэш переданного пароля
    "age"
    возраст пользователя    '''

    def __init__(self, nickname, password, age):
        if isinstance(password, str):
            self.password = hash(password)
        else:
            self.password = hash(str(password))
        if isinstance(nickname, str):
            self.nickname = nickname
        else:
            self.nickname = str(nickname)
        self.age = age

    def __str__(self):
        return f'{self.nickname}, {self.password}, {self.age}'


class Video:
    ''' Класс принимает параметры
    title (Наименование видео)
    duration (Длительность воспроизведения)
    time_now (Начало воспроизведения сек.)
    adult_mode (флак проверки на возраст)
    реализуют арибуты
    title, duration,time_now,adult_mode'''

    #  list_video = {}
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    #     self.list_video[self.title] = [self.duration,self.time_now,self.adult_mode]

    def __str__(self):
        return f'{self.title}, {self.duration}, {self.time_now}, {self.adult_mode} '


class UrTube:
    '''Реализуются возможности просмотра видео с учетом регистрации и проверки пользователей на возраст
    реализуются атрибуты
    current_user переменная содержащая текущего пользователя
    users словарь содержит массив данных с данными пользователей
    videos словарь содержит массив данных с параметрами видео
    реализованы методы
    add - добавляет в словарь данные видео
    get_videos - осуществляет поиск по видео
    watch_video - осуществляет просмотр видео
    register - регистрирует нового пользователя
    log_in - осуществляет вход существующего пользователя
    log_out - осуществляет выход пользователя'''
    current_user = None
    users = {}
    videos = {}

    def add(self, *other):
        # принимает любое количество экземпляров видео и записывает в словарь с атрибутами видео
        for v in other:
            if self.videos.get(v.title) == None:
                self.videos[v.title] = [v.duration, v.time_now, v.adult_mode]
            else:  # print(f'{v.title} уже есть в базе') можно сделать вывод сообщения для оповещения пользователя
                continue

    def get_videos(self, search_word):
        # Осуществляет поиск по словарю с атрибутами видео по части ключа
        # не зависит от регистра
        v_list = []
        if isinstance(search_word, str) == False:
            search_word = str(search_word)
        for sw in self.videos.keys():
            if search_word.upper() in sw.upper():
                v_list.append(sw)
                continue
        return v_list

    def watch_video(self, name_video):
        # Осуществляет показ видео с указанной секунды по времени длительности видео
        # осуществляет проверку или регистрацию пользователя, без регистрации видео не показывается
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        else:
            it = self.users.get(self.current_user)
            if it != None:
                age_user = it[1]
        flag_v = False
        for sk, si in self.videos.items():
            if name_video == sk:
                if si[2] == True and age_user < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    flag_v = False
                    return
                flag_v = True
            if flag_v == True:
                if si[1] > 0:
                    start = si[1]
                else:
                    start = 1
                for s in range(start, si[0] + 1):
                    print(f'{str(s)} ', end='')
                    time.sleep(1)
                print(', Конец видео')

    def register(self, nickname, password, age):
        # Регистрация новых пользователей, если пользователь существует, то выдается текст ошибки
        # и регистрация прекращается
        # данные пользователей записываются в словарь с данными пользователей
        user = User(nickname, password, age)
        if self.users.get(user.nickname) == None:
            self.users[user.nickname] = [user.password, user.age]
            self.log_in(user.nickname, user.password)
            self.current_user = user.nickname
        else:
            print(f'Пользователь {nickname} уже существует')
            return

    def log_in(self, nickname, password):
        # осуществляет вход пользователя по имени, если пользователь существует,
        # то сравнивается хэш паролей, если пароль неправильный, то вход прекращается
        it = self.users.get(nickname)
        if it != None:
            if it[1] == hash(password):
                self.current_user = nickname

    def log_out(self):
        # Осуществляет выход пользователя.
        if self.current_user != None:
            self.current_user = None


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
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
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
