class Fish:
    def __init__(self, name, weight, speed):
        self.name = name
        self.weight = weight
        self.speed = speed
    def run(self):
        print(f'Я плыву со скоростью {self.speed}')

class Fish(Fish):
    def __init__(self, name, weight, speed, tail_length):
        super().__init__(name, weight, speed)
        self.__tail_length = tail_length
    def bup(self):
        print('bupbup')
    def wag_tail(self):
        print(f'Хвост размером {self.__tail_length} виляет при плавании')

my_fish = Fish('kurp', 3, 13, 2)
# print(my_fish.__tail_length) защищённый аттрибут
my_fish.wag_tail()
print(my_fish.name)
print(my_fish.weight)
my_fish.bup()