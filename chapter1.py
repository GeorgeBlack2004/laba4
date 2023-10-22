import math


class Triangle:
    def check(self, a, b, c):
        if a > b + c or b > a + c or c > a + b:
            return False
        return True

    def square(self, a, b, c):
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def perimeter(self, a, b, c):
        return a + b + c


a1 = int(input("Введите первую сторону: "))
b1 = int(input("Введите вторую сторону: "))
c1 = int(input("Введите третью сторону: "))

prov_ = Triangle()
prov = prov_.check(a1, b1, c1)
if prov == 0:
    print("Это не может быть треугольником!")
else:
    print("Это треугольником!")
    S1 = prov_.square(a1, b1, c1)
    P1 = prov_.perimeter(a1, b1, c1)
    print("Площадь треугольника: ", "%.2f" % S1)
    print("Периметр треугольника: ", P1)
