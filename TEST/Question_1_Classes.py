class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self.__is_square = True

    @property
    def area(self):
        try:
            area = self.length * self.width
            if area < 0:
                area = area*-1
                return area
            else:
                return area
        except ValueError:
            print("Please enter a number")

    @property
    def perimeter(self):
        try:
            perimeter = 2 * (self.length + self.width)
            if self.length < 0:
                perimeter = 2 * self.width
                return perimeter
            elif self.width < 0:
                perimeter = 2 * self.length
                return perimeter
            elif self.length and self.width < 0:
                perimeter = 0
                return perimeter
            else:
                return perimeter
        except ValueError:
            print("Please enter a number")

    @property
    def is_square(self):
        if self.length == self.width:
            return self.__is_square
        else:
            return False
