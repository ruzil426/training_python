team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score1 + score2
time_avg = round((team1_time + team2_time)/tasks_total, 1)

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = ('Победа команды Мастера кода!')
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = ('Победа команды Волшебники Данных!')
else:
    result = ('Ничья!')

print("В команде Мастера кода участников: %s! " % team1_num)
print("Итого сегодня в командах участников: %(p1)s и %(p2)s !" % {'p1': team1_num, 'p2': team2_num})

print("Команда Волшебники данных решила задач: {} !".format(score2))
print("Волшебники данных решили задачи за {} с !".format(team1_time))

print(f'"Команды решили {score1} и {score2} задач.”')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

print(result)