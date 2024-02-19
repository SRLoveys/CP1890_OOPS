from dataclasses import dataclass


@dataclass
class Rectangle:
    height: int
    width: int

    @property
    def area(self):
        return self.height * self.width

    @property
    def perimeter(self):
        return 2 * (self.height + self.width)


def draw_rectangle(base, height):
    for b in range(0, int(base)):
        print('*', end='  ')
    print()
# Condition needed to draw the correct number of lines
    if base != 1:
        for h in range(0, int(height - 2)):
            print('* ' + '   ' * int(base - 2) + ' *')
    else:
        for h in range(0, int(height - 2)):
            print('* ' + '   ' * int(base - 2))
# Condition needed to draw the correct number of lines
    if height != 1:
        for b in range(0, int(base)):
            print('*', end='  ')
        print()


def main():
    print('\nRectangle Program\n')
    while True:
        base = int(input('Enter base: '))
        height = int(input('Enter height: '))
        rectangle = Rectangle(height, base)
        print('Area: ', rectangle.area)
        print('Perimeter: ', rectangle.perimeter)

        draw_rectangle(rectangle.width, rectangle.height)

        loop = input('\nContinue? (y/n): ')
        if loop == 'n':
            break
        else:
            print()


if __name__ == '__main__':
    main()
    print('\nBye!')
