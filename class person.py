class person:
    def __init__(self):
        self.name = "วรวุฒิ"
        self.age = 18
        self.__salary = 50000

P = person()
print(P.name)
print(P.age)
# print(P.__salary)
print(P.__persen__salary)