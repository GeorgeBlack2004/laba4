class Calculator:
    def __init__(self, number_one, number_two):
        self.num1 = number_one
        self.num2 = number_two

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Ошибка! Деление на ноль недопустимо."

    @classmethod
    def square(cls, num):
        return num ** 2

    @classmethod
    def exponentiation(cls, num1, num2):
        return pow(num1, num2)


number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))

calculator = Calculator(number_1, number_2)
print("Сумма:", calculator.add())
print("Разность:", calculator.subtract())

result = Calculator.multiply(number_1, number_2)
print("Произведение:", result)

result = Calculator.divide(number_1, number_2)
print("Частное:", "%.2f" % result)

result_1 = Calculator.square(number_1)
result_2 = Calculator.square(number_2)
print("Квадрат числа", number_1, ":", result_1)
print("Квадрат числа", number_2, ":", result_2)

result_1 = Calculator.exponentiation(number_1, number_2)
result_2 = Calculator.exponentiation(number_2, number_1)
print(f"Возведение числа {number_1} в {number_2}:", result_1)
print(f"Возведение числа {number_2} в {number_1}:", result_2)
