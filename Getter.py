class Animal:
    def __init__(self, sound):
        self.__sound = sound
        
    def get_sound(self):
        return self.__sound
    
animal = Animal("เมี๊ยว")
print(animal.get_sound())