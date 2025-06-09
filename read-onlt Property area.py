class circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

c = circle(5)
print("พื้นที่วงกลม:", c.area)  # แสดงผลพื้นที่วงกลม