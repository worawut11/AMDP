class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.sound)

animal = Animal("แมว", "เมี๊ยว")
animal.make_sound()