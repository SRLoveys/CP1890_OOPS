def title():
    print('Rectangles test')


def get_base_height():
    while True:
        base = float(input('Enter base: '))
        height = float(input('Enter height: '))
        if base > 99 or height > 99:
            print('too big')
        else:
            return base, height


def get_area_perimeter(base, height):
    return base * height, (base * 2) + (height * 2)


def draw_rectangle(base, height):
    for b in range(0, int(base)):
        print('*', end='  ')
    print()
    for h in range(0, int(height - 2)):
        print('* ' + '   ' * int(base - 2) + ' *')
    if height != 1:
        for b in range(0, int(base)):
            print('*', end='  ')
        print()


def main():
    title()
    while True:
        base, height = get_base_height()
        area, perimeter = get_area_perimeter(base, height)
        print('Area: ', area)
        print('Perimeter: ', perimeter)
        draw_rectangle(base, height)

        # loop = input('continue? (y/n): ')
        # if loop == 'n':
        #     break


if __name__ == '__main__':
    main()