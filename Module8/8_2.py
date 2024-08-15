def personal_sum(numbers):
    result = 0
    numb_of_elem = 0
    incorrect_data = 0
    try:
        for number in numbers:
            try:
                result += number
                numb_of_elem += 1
            except TypeError:
               incorrect_data += 1
               print(f'Некорректный тип данных для подсчёта суммы - {number}')
    except TypeError:
        print(f'Передана не коллекция - {numbers}')
        return None
    print(f'Количество некорретных данных {incorrect_data}')
    return result/numb_of_elem

def calculate_average(numbers):
    try:
        average = personal_sum(numbers)
        return average
    except ZeroDivisionError:
        print('В numbers записан некорректный тип данных')
        return 0

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
