class Employee:
    def __init__(self, name, salary, seniority):
        self.name = name
        self.salary = salary
        self.seniority = seniority
        self.grade = 0

    def up(self):
        self.salary += 100

    def print(self):
        print(f'Сотрудник {self.name}, зарплата {self.salary}')

    def grade_up(self):
        self.grade += 1

    def check_if_it_is_time_for_upgrade(self):
        pass


ivan = Employee('Иван', 100)
ivan.up()
ivan.print()
