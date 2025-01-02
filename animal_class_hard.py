from random import randint

class Animal: #Класс обладает следующими атрибутами:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self,speed):  #Объект этого класса обладает следующими атрибутами:
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        x = self._cords[0] + dx * self.speed
        y = self._cords[1] + dy * self.speed
        z = self._cords[2] + dz * self.speed
        if z < 0:
            print("It's too deep, i can't dive")
        else:
            self._cords = [x, y, z]


    def get_cords(self):
        print(f'X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    beak = True # атрибут класса
    def lay_eggs(self):# метод класса
        num_eggs = randint(1, 7)
        print(f"Here are(is) {num_eggs} eggs for you")


class  AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 4 # атрибут класса
    def dive_in(self, dz):
        z = self._cords[2] - abs(dz) *  (self.speed / 2)
        self._cords[2] = int(min(z, 0))   # почему при ошибке self._cords(не указан индекс) = max(z, 0)
                                         # показывает ошибку в get_cords???


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 9


class Duckbill( PoisonousAnimal, Bird, AquaticAnimal):
    sound =  "Click-click-click"
    def __init__(self, speed):
        super().__init__(speed)
    def speak(self):
        print(self.sound)



db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 6)
db.get_cords()
db.dive_in(1)
db.get_cords()
db.lay_eggs()
