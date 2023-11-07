class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} двигается")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}.")

    def show_speed(self):
        print(f"Текущая скорость {self.name} это {self.speed} км/ч.")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Скорость превышена!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Скорость превышена!")


class PoliceCar(Car):
    pass


car1 = TownCar(70, "красная", "Audi", False)
car2 = SportCar(120, "синяя", "Ferrari", False)
car3 = WorkCar(30, "белая", "Ford", False)
car4 = PoliceCar(90, "черная", "Police Car", True)

car1.go()
car1.show_speed()
car1.turn("налево")
car1.stop()

car2.go()
car2.show_speed()
car2.turn("направо")
car2.stop()

car3.go()
car3.show_speed()
car3.turn("направо")
car3.stop()

car4.go()
car4.show_speed()
car4.turn("налево")
car4.stop()
