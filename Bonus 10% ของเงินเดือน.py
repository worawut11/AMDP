class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("เงินเดือนต้องไม่เป็นค่าลบ")
        else:
            self.__salary = value

    def get_bonus(self):
        return self.__salary * 0.1

emp = Employee("สมชาย", 30000)
print("โบนัส", emp.get_bonus())  # แสดงผล 3000.0