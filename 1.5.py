cash = int(input('Пожалуйста, введите вашу выручку'))
costs = int(input('Пожалуйста, введите ваши издержки'))
if cash > costs:
    print('Поздравляем, вы в плюсе')
    rent = (cash - costs) / cash
    print(f'Рентабельность составила: {rent}')
    pers = int(input('Пожалуйста, введите количество сотрудников'))
    one_pers = (cash - costs) / pers
    print(f'Прибыль на одного сотрудника: {one_pers}')
elif costs > cash:
    print('Увы, вы отработали в минус')
else:
    print('Увы, вы ничего не заработали')
