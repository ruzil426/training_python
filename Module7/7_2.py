file_name = 'test.txt'
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
def custom_write(file_name, info):
    file_append = open(file_name, 'a', encoding = 'utf-8')
    line_number = 0
    for i in info:
        line_number += 1
        byte = file_append.tell()
        file_append.write(i + '\n')
        string_positions = {(line_number, byte): i}
        for elem in string_positions.items():
            print(elem)
    file_append.close()
    return string_positions

custom_write(file_name, info)