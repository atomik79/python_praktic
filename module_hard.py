import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user

    def add(self, *args):
        for movie in args:
            if movie not in self.videos:
                self.videos.append(movie)

    def get_videos(self, text):
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie


    def watch_video(self, movie):
        if not self.current_user:
            print("Выполните вход")
            return

        for x in self.videos:
            if x.title == movie:
                if x.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет")
                    return

                for i in range(1, 11):
                    print(i, end=' ')
                    time.sleep(1)
                    x.time_now += 1
                x.time_now = 0
                print("Конец video")

if __name__ == '__main__':

    urTube = UrTube()
    v1 = Video("Лучший язык программирования 2024 года", 200)
    v2 = Video("Для чего девушкам парень программист?", 10, adult_mode=True)

urTube.add(v1, v2)  # добавление видео

print(urTube.get_videos("Лучший"))
print(urTube.get_videos("ПРОГ"))
urTube.watch_video("Для чего девушкам парень программист?")
urTube.register('vasya_pupkin', 'lolkekcheburek', 13)
urTube.watch_video("Для чего девушкам парень программист?")
urTube.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
urTube.watch_video("Для чего девушкам парень программист?")
urTube.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(urTube.current_user)
urTube.watch_video('Лучший язык программирования 2024 года!')