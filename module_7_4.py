def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды "Мастера кода"!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды "Волшебники Данных"!'
    else:
        result = 'Ничья!'
    return result

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

print('В команде "Мастера кода" участников: %s !' % team1_num)
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
print('Команда "Мастера кода" решила задач: {} !'.format(score_1))
print('Команда "Волшебники данных" решила задач: {time} !'.format(time=score_2))
print('"Волшебники данных" решили задачи за {} с.'.format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result()}')
print(f'Сегодня было решено {score_1 + score_2} задач, '
      f'в среднем по {round((team1_time + team2_time) / (score_1 + score_2), 1)} секунды на задачу.')
