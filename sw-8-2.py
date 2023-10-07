class Fish:
    def __init__(self, name, weight, speed):
        self.name = name
        self.weight = weight
        self.speed = speed

    def run(self):
        print(f'Я плыву со скоростью {self.speed}')


my_fish = Fish('karp', 3, 13)

print(my_fish.name)
print(my_fish.weight)
my_fish.run()