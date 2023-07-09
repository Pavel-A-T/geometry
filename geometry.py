import math
from abc import ABC, abstractmethod


class Shape(ABC):

    # При помощи ООП спроектировать и реализовать геометрический калькулятор для вычислений, производимых над фигурами.
    # Калькулятор должен поддерживать вычисления для плоских и объемных фигур.

    # Плоские фигуры: круг, квадрат, прямоугольник, треугольник, трапеция, ромб.
    # Объемные фигуры: сфера, куб, параллелепипед, пирамида, цилиндр, конус.
    # Реализовать как минимум один общий метод вычисления для всех фигур и как минимум один специфичный для определенных фигур.
    # Например, площадь – общий метод для всех фигур, медиана – специфичный метод для ряда фигур.

    # Реализовать интерфейс программы для возможности взаимодействия пользователя с ней.
    # Интерфейс может быть консольным или графическим.

    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):
    def get_answer(self):
        d = float(input("Введите диаметр окружности:  "))
        print("Площадь окружности равна:")
        print(self.get_area(d))

    def get_area(self, d):
        return round(math.pi * d * d / 4, 3)


class Rectangle(Shape):

    def get_answer(self):
        side_a = float(input("Введите ширину прямоугольника:  "))
        side_b = float(input("Введите высоту прямоугольника:  "))
        print("Площадь прямоугольника равна:")
        print(self.get_area(side_a, side_b))

    def get_area(self, side_a, side_b):
        return side_a * side_b


class Square(Rectangle):

    def get_answer(self):
        side_a = float(input("Введите размер стороны квадрата:  "))
        print("Площадь квадрата равна:")
        print(self.get_area(side_a, side_a))


class Triangle(Shape):

    def get_answer(self):
        side_a = float(input("Введите сторону а треугольника:  "))
        side_b = float(input("Введите сторону в треугольника:  "))
        side_c = float(input("Введите сторону c треугольника:  "))
        if self.check_triangle(side_a, side_b, side_c):
            print("Площадь треугольника равна:")
            print(self.get_area(side_a, side_b, side_c))
            self.get_median_a(side_a, side_b, side_c)

    def check_triangle(self, a, b, c):
        try:
            if (a + b < c or a + c < b or c + b < a):
                print("Две стороны треугольника в сумме должны быть больше третьей по длине!")
                raise Exception()
        except:
            return False
        return True

    def get_area(self, side_a, side_b, side_c):
        p = (side_a + side_b + side_c) / 2
        return round(math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c)), 3)

    def get_median_a(self, side_a, side_b, side_c):
        print(f"Медиана стороны а = {side_a} равна: ")
        print(round((math.sqrt(2 * (side_b ** 2 + side_c ** 2) - side_a ** 2) / 2), 3))


class Trapezoid(Shape):
    def get_answer(self):
        side_a = float(input("Введите основание а трапеции:  "))
        side_b = float(input("Введите основание в трапеции:  "))
        h = float(input("Введите высоту трапеции:  "))
        print("Площадь трапеции равна:")
        print(self.get_area(side_a, side_b, h))

    def get_area(self, side_a, side_b, h):
        return round((side_a + side_b) * h / 2, 3)


class Rhomb(Shape):
    def get_answer(self):
        side_a = float(input("Введите размер диагонали ромба а:  "))
        side_b = float(input("Введите  размер диагонали ромба в:  "))
        print("Площадь ромба равна:")
        print(self.get_area(side_a, side_b))

    def get_area(self, side_a, side_b):
        return round(side_a * side_b / 2, 3)


class Sphere(Circle):
    def get_answer(self):
        d = float(input("Введите диаметр сферы:  "))
        print("Площадь сферы равна:")
        print(self.get_area(d))

    def get_area(self, d):
        return round(super().get_area(d) * 4, 3)


class Cube(Square):
    def get_answer(self):
        side_a = float(input("Введите размер стороны куба:  "))
        print("Площадь куба равна:")
        print(round(super().get_area(side_a, side_a) * 6, 3))


class Parallelepiped(Rectangle):
    def get_answer(self):
        side_a = float(input("Введите сторону а параллелепипеда:  "))
        side_b = float(input("Введите сторону в параллелепипеда:  "))
        h = float(input("Введите высоту параллелепипеда:  "))
        print("Площадь параллелепипеда равна:")
        print(round(super().get_area(side_a, side_b) + super().get_area(side_a, h) + super().get_area(side_b, h), 3))


class Pyramid(Rectangle, Triangle):

    def get_answer(self):
        side_a = float(input("Введите сторону основания пирамиды (считаем, что это правильная пирамида):  "))
        h = float(input("Введите высоту пирамиды:  "))
        print("Площадь пирамиды равна:")
        side_b = math.sqrt((side_a / 2) ** 2 * h ** 2)
        print(round(super().get_area(side_a, side_a) * side_b / 2, 3))
        super().get_median_a(side_a, side_b, side_b)


class Cylinder(Circle):
    def get_answer(self):
        d = float(input("Введите диаметр основания цилиндра:  "))
        h = float(input("Введите высоту цилиндра:  "))
        print("Площадь цилиндра равна:")
        print(self.get_area(d, h))

    def get_area(self, d, h):
        radius = d / 2
        s = 2 * math.pi * radius * h
        return round(2 * super().get_area(d) + s, 3)


class Cone(Circle):
    def get_answer(self):
        d = float(input("Введите диаметр окружности основания конуса:  "))
        h = float(input("Введите высоту конуса:  "))
        print("Площадь конуса равна:")
        print(self.get_area(d, h))

    def get_area(self, d, h):
        radius = d / 2
        s = math.pi * radius * math.sqrt(radius ** 2 + h ** 2)
        return round(super().get_area(d) + s, 3)
