import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return self.nickname == other.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title.lower() == other.title.lower()

    def __str__(self):
        return self.title, self.duration, self.adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname in users and password == hash(password):
                self.current_user = user

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if user not in self.users:
            self.users.append(user)
            self.current_user = user
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_out(self):
        if self.current_user:
            self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, word):
        result = []
        for video in self.videos:
            if word.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, film):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for video in self.videos:
                if film != video.title:
                    continue
                elif video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                else:
                    for second in range(video.time_now + 1, video.duration + 1):
                        print(second, end=' ', flush=True)
                        time.sleep(1)
                    print("Конец видео")
                    video.time_now = 0
                    return


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