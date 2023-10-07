class Fish:
    def make_noise(self):
        pass

class Fish(Fish):
    def make_noise(self):
        print('pub...pub...pub')

class Shark(Fish):
    def make_noise(self):
        print('bulk... bulk... bulk')

my_fish = Fish()
my_shark = Shark()

my_fish.make_noise()
my_shark.make_noise()