class Student:
    def __init__(self, name='Ivan', age=18, group_number='10A'):
        self.name = name
        self.age = age
        self.groupNumber = group_number

    def get_name(self):
        return f'Имя студента - {self.name}'

    def get_age(self):
        return f'возраст студента - {self.age}'

    def get_group_number(self):
        return f'группа студента - {self.groupNumber}.'

    def set_name_age(self, name, age):
        self.name = name
        self.age = age
        return f'Имя студента - {self.name}, возраст студента - {self.age}'

    def set_group_number(self, group_number):
        self.groupNumber = group_number
        return f'группа студента - {self.groupNumber}.'


Petya = Student("Петя", 18, "03b")
Masha = Student("Маша", 21, "3k")
Ivan = Student()
Michail = Student()
Sara = Student("Сара", 16, "11AA")
print(f'{Petya.get_name()}, {Petya.get_age()}, {Petya.get_group_number()}')
print(f'{Masha.get_name()}, {Masha.get_age()}, {Masha.get_group_number()}')
print(f'Имя студента - {Ivan.name}, возраст студента - {Ivan.age}, группа студента - {Ivan.groupNumber}.')
print(f'{Michail.set_name_age("George", 30)}, {Michail.set_group_number("0303SDE")}')
print(f'{Sara.get_name()}, {Sara.get_age()}, {Sara.get_group_number()}')
