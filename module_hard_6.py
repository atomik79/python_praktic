from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = sides
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
         if 0 <= r <= 255 and 0 <= r <= 255 and 0 <= r <= 255:
             return r, g, b
         else:
             return self.__color

    def set_color(self, r, g, b):
        new_color = self.__is_valid_color(r, g, b)
        if new_color:
            self.__color = list(new_color)
            return  list(new_color)
        else:
            return self.__color

    def __is_valid_sides(self, *sides):
        for i in sides:
            if i > 0 and len(sides) == self.sides_count:
                return True
            else:
                return False


    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) != self.sides_count:
            return self.__sides
        else:
            self.__sides = list(new_sides)
            return list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = sides
        self.__radius = self.__sides[0] / (2 * pi)

    def get_square(self):
        return pi * pow(self.__radius, 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        p = sum(self.get_sides()) * 0.5
        return sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) == 1:
            self.set_sides(*([self.get_sides()[0]] * self.sides_count))

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self._Figure__sides = [new_sides[0]] * self.sides_count
            print(self._Figure__sides)
        elif self._Figure__is_valid_sides(*new_sides):
            self._Figure__sides = list(new_sides)

    def get_volume(self):
        side = self.get_sides()[0]
        return pow(side, 3)


circle = Circle((200, 200, 100), 10, 15, 6)
triangle = Triangle((200, 200, 100), 10, 6)
cube = Cube((200, 200, 100), 9, 12)
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())