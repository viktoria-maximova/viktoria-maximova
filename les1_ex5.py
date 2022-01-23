
# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

revenue = int (input ('Выручка: '))
costs = int (input ('Издержки: '))
fin_result = revenue - costs

if fin_result > 0:
    print (f'Прибыль составляет {fin_result}')
    profitability = fin_result/revenue
    print(f'Рентабельность составляет {profitability}')
    persons = int(input('Численность сотрудников: '))
    profit_per_person = profitability / persons
    print(f'Прибыль фирмы в расчете на одного сотрудника составляет {profit_per_person}')

elif fin_result == 0:
    print(f'Прибыль составляет 0')

else:
    print(f'Убыток составляет {-fin_result}')


