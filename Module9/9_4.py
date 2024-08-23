first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: [x[i] == y[i] for i in range(len(x))], first, second))

print(result)
#####

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding = 'utf-8') as file:
            for i in data_set:
                file.write(str(i) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#####

from random import choice
class MysticBall:
    def __init__(self, *word):
        self.word = word
    def __call__(self):
        elem = choice(self.word)
        return elem

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())