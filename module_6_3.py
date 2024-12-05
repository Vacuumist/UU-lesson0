from random import randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._coords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self._coords[0] += dx * self.speed
        self._coords[1] += dy * self.speed
        if self._coords[2] + dz * self.speed >= 0:
            self._coords[2] += dz * self.speed
        else:
            print("It's too deep, i can't dive :(")

    def get_coords(self):
        print(f'X: {self._coords[0]}, Y: {self._coords[1]}, Z: {self._coords[2]}')


    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs = randint(1,4)
        if eggs == 1:
            print(f'Нere is an egg for you')
        else:
            print(f'Нere are {eggs} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._coords[2] -= int(abs(dz) * self.speed / 2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_coords()
db.dive_in(6)
db.get_coords()
db.lay_eggs()
