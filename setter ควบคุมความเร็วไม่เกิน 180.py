class Car:
    def __init__(self, speed=0):
        self.speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Speed cannot be negative.")
        elif value > 180:
            raise ValueError("Speed cannot exceed 180 km/h.")
        self._speed = value
        def drive(self):
            print(f"Driving at {self.speed} km/h")
            
c = Car("Toyota,150")
c.speed = 200  # Set speed to 100 km/h
c.speed = 170  # This will raise an error
c.drive()  # Output: Driving at 170 km/h