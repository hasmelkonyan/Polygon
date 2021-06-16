import math

class Polygon:
    sides = []
    def __init__(self, side):
        self.side = side

        if not isinstance(side, int):
            try:
                raise AttributeError
            except AttributeError as e:
                print("Only integers are allowed")


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
            return f"This polygon has a {self.side} side"



    def input_side(self):
        for i in range(len(self.sides)):
            self.sides[i] = input("input value of side")

    def area(self):
        pass

    def perimeter(self):
        p = 0
        for i in range(len(self.sides)):
            p += self.sides[i]
        return p



class Triangle(Polygon):
    sides = [0, 0, 0]
    def __init__(self):
        super().__init__(3)

    def type_of_polygon(self):
        if self.sides[0] != self.sides[1] != self.sides[2]:
            return "Triangle is simple"
        elif self.sides[0] == self.sides[1] == self.sides[2]:
            return "Triangle is isosceles"
        elif self.sides[0] == self.sides[1] != self.sides[2] and self.sides[0] + self.sides[1] > self.sides[2] \
                or self.sides[0] == self.sides[2] != self.sides[1] and self.sides[0] + self.sides[2] > self.sides[1] \
                or self.sides[1] == self.sides[2] != self.sides[0] and self.sides[1] + self.sides[2] > self.sides[0]:
            return "Two side equal triangle"
        else:
            print("impossible triangle")

    def area(self):
        s = (self.sides[0] + self.sides[1] + self.sides[2]) / 2
        area = math.sqrt(s * ((s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2])))
        return area


class Rectangle(Polygon):
    sides = [0, 0, 0, 0]
    def __init__(self):
        super().__init__(4)

    def type_of_polygon(self):
        if self.sides[0] == self.sides[1] == self.sides[2] == self.sides[3]:
            return "square"
        elif self.sides[0] == self.sides[2] and self.sides[1] == self.sides[3] and \
                self.sides[0] != self.sides[1]:
            return "rectangle"
        else:
            return "tetragon"





