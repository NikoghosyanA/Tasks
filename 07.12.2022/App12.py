class Dot:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return 'точка: x = {}, y = {}'.format(self.__x, self.__y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        if isinstance(x, int):
            self.__x = x
        else:
            raise Exception('Вы ввели "x" не число.')

    def set_y(self, y):
        if isinstance(y, int):
            self.__y = y
        else:
            raise Exception('Вы ввели "x" не число.')


dot = Dot(1, 1)
print(dot)
print(dot.get_x())
print(dot.get_y())
new_x = 7
new_y = 9
dot.set_x(new_x)
dot.set_y(new_y)
print(dot.get_x())
print(dot.get_y())
