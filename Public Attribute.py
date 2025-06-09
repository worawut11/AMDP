class Animal:
    def __init__(self, name):
        self.__name = name

animal = Animal("แมว")
print(animal._Animal__name)