class Car:
    def __init__(self, model, vin, number):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        else:
            self.__vin = 0
        if self.__is_valid_numbers(number):
            self.__number = number
        else:
            self.__number = 0
        if self.__vin != 0 and self.__number != 0:
            print(f'{self.model} успешно создан')

    def __is_valid_vin(self, vin):
        try:
            if not isinstance(vin, int):
                raise Correct_Vin('Некорректный тип vin номер')
            elif vin < 1000000 or vin > 9999999:
                raise Correct_Vin('Неверный диапазон для vin номера')
            else:
                return True
        except Correct_Vin as exc:
            print(exc.message_vin)

    def __is_valid_numbers(self, number):
        try:
            if not isinstance(number, str):
                raise Correct_Car_Number('Некорректный тип данных для номеров')
            elif len(number) != 6:
                raise Correct_Car_Number('Неверная длина номера')
            else:
                return True
        except Correct_Car_Number as exc:
            print(exc.message_number)

class Correct_Vin(Exception):
    def __init__(self, message_vin):
        self.message_vin = message_vin

class Correct_Car_Number(Exception):
    def __init__(self, message_number):
        self.message_number = message_number

first = Car('Model1', 1000000, 'f123dj')
second = Car('Model2', 300, 'т001тр')
third = Car('Model3', 2020202, 'нет номера')