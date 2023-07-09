from geometry import Circle, Cone, Cube, Cylinder, Parallelepiped, Pyramid, Rectangle, Rhomb, Sphere, Square, Trapezoid, \
    Triangle

class Main:
    def start(self):
        print(""" Выберите фигуру: 1 - прямоугольник
                  2 - квадрат
                  3 - треугольник 
                  4 - окружность
                  5 - трапеция
                  6 - ромб
                  7 - конус
                  8 - цилиндр
                  9 - сфера
                  10 - куб
                  11 - параллелепипед
                  12 - пирамида
        """)
        choice = int(input("Введите число:  "))
        if choice == 1:
            rectangle = Rectangle()
            rectangle.get_answer()
        elif choice == 2:
            square = Square()
            square.get_answer()
        elif choice == 3:
            triangle = Triangle()
            triangle.get_answer()
        elif choice == 4:
            circle = Circle()
            circle.get_answer()
        elif choice == 5:
            trapezoid = Trapezoid()
            trapezoid.get_answer()
        elif choice == 6:
            rhomb = Rhomb()
            rhomb.get_answer()
        elif choice == 7:
            cone = Cone()
            cone.get_answer()
        elif choice == 8:
            cylinder = Cylinder()
            cylinder.get_answer()
        elif choice == 9:
            sphere = Sphere()
            sphere.get_answer()
        elif choice == 10:
            cube = Cube()
            cube.get_answer()
        elif choice == 11:
            parallelepiped = Parallelepiped()
            parallelepiped.get_answer()
        elif choice == 12:
            pyramid = Pyramid()
            pyramid.get_answer()
        else:
            print("Завершение работы.")


main = Main()
main.start()
