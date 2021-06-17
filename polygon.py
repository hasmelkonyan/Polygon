import math


class Polygon:
    def __init__(self, side):
        self.side = side

    def type_of_polygon(self):
        if self.side < 3:
            return "This is a not polygon"
        elif self.side == 3:
            return "this is a triangle"
        elif self.side == 4:
            return "This is a quadrangle"
        elif self.side == 5:
            return "This is a pentagon"
        else:
            return f"This polygon has a {self.side}"

    def area(self):
        pass

    def parimeter(self):
        pass


class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__(3)
        self.a = a
        self.b = b
        self.c = c




    def type_of_polygon(self):
        if self.a != self.b != self.c:
            return "Triangle is simple"
        elif self.a == self.b == self.c:
            return "Triangle is isosceles"
        elif self.a == self.b != self.c and self.a + self.b > self.c \
                or self.a == self.c != self.b and self.a + self.c > self.b \
                or self.b == self.c != self.a and self.b + self.c > self.a:
            return "Two side equal triangle"
        else:
            print("impossible triangle")

    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * ((s - self.a) * (s - self.b) * (s - self.c)))
        return area

    def parimeter(self):
        return self.a + self.b + self.c


class Rectangle(Polygon):
    def __init__(self,height, width):
        super().__init__(4)
        self.height = height
        self.width = width
        self.__angle = 90



    def get_angle(self):
        return self.__angle

    def type_of_polygon(self):
        if self.width == self.height:
            return "square"
        else:
            return "rectangle"

    def area(self):
        return self.width * self.height

    def parimeter(self):
        return (self.width + self.height) * 2


# class TriOrRect(Triangle, Rectangle):
#     def __init__(self, side, a, b, c, width, height):
#         Triangle.__init__(self, a, b, c)
#         Rectangle.__init__(self, width, height)
#         self.side = side
#
#     def type_of_polygon(self):
#         if self.side == 3:
#             return Triangle.type_of_polygon(self)
#         elif self.side == 4:
#             return Rectangle.type_of_polygon(self)
#         else:
#             return Polygon.type_of_polygon(self)
#
#     def area(self):
#         if self.side == 3:
#             return Triangle.area(self)
#         elif self.side == 4:
#             return Rectangle.area(self)
#         else:
#             return Polygon.area(self)
#
#     def parimeter(self):
#         if self.side == 3:
#             return Triangle.parimeter(self)
#         elif self.side == 4:
#             return Rectangle.parimeter(self)
#         else:
#             return Polygon.parimeter(self)


if __name__ == '__main__':
    shape = Triangle(5,2,4)
    print(shape.type_of_polygon())
    print(shape.area())

