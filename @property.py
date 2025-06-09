class Animal:
    def __init__(self, sound):
        self.__sound = sound

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, value):
        if value != "":
            self.__sound = value
        else:
            print("เสียงไม่สามารถเป็นค่าว่างได้")

animal = Animal("เมี๊ยว")
animal.sound = ""  # จะไม่เปลี่ยนแปลงค่าเสียง
animal.sound = "โฮ่ง"  # จะเปลี่ยนแปลงค่าเสียงเป็น "โฮ่ง"
print(animal.sound)  # แสดงผล "โฮ่ง"