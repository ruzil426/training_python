class Vehicle():
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def get_model(self):
        return self.__model
    def get_horsepower(self):
        return self.__engine_power
    def get_color(self):
        return self.__color
    def print_info(self):
        print('Модель: ', self.__model)
        print('Мощность двигателя: ', self.__engine_power)
        print('Цвет: ', self.__color)
        print('Владелец: ', self.owner)
    def set_color(self, new_color):
        if new_color.casefold() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print('Нельзя сменить цвет на ', new_color)
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark 2', 'blue', 500)

vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()