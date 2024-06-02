class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.go_to()
    def go_to(self):
        print(f'ЖК "{self.name}", всего этажей {self.number_of_floors}')
        print('Введите номер этажа')
        new_floor = int(input())
        if new_floor <= self.number_of_floors and new_floor >= 1:
            for i in range(1, new_floor+1):
                print(i)
        else: print('Такого этажа не существует')

h1 = House('ПИК', 10)
h2 = House('Высота', 5)
