class Animal:
    def __init__(self, sound):
        self.__sound = sound

    def set_sound(self, sound):
        if sound != "":
            self.__sound = sound
        else:
            print("เสียงไม่สามารถเป็นค่าว่างได้")

    def get_sound(self):
        return self.__sound

animal = Animal("เมี๊ยว")
animal.set_sound("")
animal.set_sound("โฮ่ง")
print(animal.get_sound())