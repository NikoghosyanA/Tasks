class Country:
    country_name = ''
    area = 100000
    population = 22000000

    def __init__(self):
        print("Это конструктор без параметров")

    def __init__(self, name):
        print("Это конструктор с параметрами")
        self.name = name

    def get_name(self):
        return self.country_name

    def get_area(self):
        return self.area

    def get_population(self):
        return self.population

    def set_name(self):
        while True:
            new_name = input()
            if new_name.isalpha() and new_name == new_name.capitalize():
                self.country_name = new_name
                break
            else:
                print('Неправильное название страны(попробуйте с большой буквы) ')

    def set_area(self):
        while True:
            new_area = input()
            if new_area.isdecimal():
                self.area = float(new_area)
                break
            else:
                print('Неправильный ввод')

    def set_population(self):
        while True:
            new_population = input()
            if new_population.isdecimal():
                self.population = int(new_population)
                break
            else:
                print('Неправильный ввод')

    def out(self):
        print(self.country_name)
        print(self.area)
        print(self.population)

    def change_population(self):
        n = int(input())
        self.population += n

    def get_r(self):
        return self.population / self.area
