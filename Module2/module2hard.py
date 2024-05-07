import random
list1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in list1:
    paste1 = random.choice(list1)
    print('1-е поле:', paste1)
    break

while 1 > 0:
    for j in list2:
        one_ = random.choice(list2)
        two_ = random.choice(list2)
        break
    str1 = str(one_)
    str2 = str(two_)
    paste2 = str1 + str2
    paste2 = int(paste2)
    sum_ = (one_+two_)

    if paste1 % sum_ == 0:
        print('2-е поле:', paste2)
        print('Сумма чисел 2-го поля =', sum_)
        break
