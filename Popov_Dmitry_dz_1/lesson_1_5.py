# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

revenue = int(input("Введите сумму выручки: "))
costs = int(input("Введите сумму издержек: "))

if revenue > costs:
    print(f"Финансовый результат: прибыль на сумму {revenue - costs}")
    profitability = revenue - (revenue - costs) # рентабельность
    print(f"Рентабильность составила: {profitability}")
    staff_amount = int(input("Веедите количество сотрудников: ")) # количество сотрудников
    profit = revenue - costs # прибыль
    profit_per_employee = profit / staff_amount # прибыль фирмы в расчёте на одного сотрудника
    print(f"Прибыль фирмы в расчёте на одного сотрудника: {profit_per_employee:.2f}")
else:
    print(f"Финансовый результат: убытки на сумму {costs -  revenue}\nУвольте нафиг своих маркетологов!")