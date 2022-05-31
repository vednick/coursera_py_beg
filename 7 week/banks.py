# Некоторый банк хочет внедрить систему управления счетами клиентов,
# поддерживающую следующие операции:
#
# Пополнение счета клиента.
# Снятие денег со счета.
# Запрос остатка средств на счете.
# Перевод денег между счетами клиентов.
# Начисление процентов всем клиентам.
#
# Вам необходимо реализовать такую систему. Клиенты банка
# идентифицируются именами (уникальная строка, не содержащая пробелов).
# Первоначально у банка нет ни одного клиента. Как только для клиента
# проводится операция пополнения, снятия или перевода денег, ему
# заводится счет с нулевым балансом. Все дальнейшие операции проводятся
# только с этим счетом. Сумма на счету может быть как положительной,
# так и отрицательной, при этом всегда является целым числом.
#
# Формат ввода
# Входной файл содержит последовательность операций. Возможны следующие
# операции:
#
# DEPOSIT name sum - зачислить сумму sum на счет клиента name. Если
# у клиента нет счета, то счет создается.
#
# WITHDRAW name sum - снять сумму sum со счета клиента name. Если
# у клиента нет счета, то счет создается.
#
# BALANCE name - узнать остаток средств на счету клиента name.
#
# TRANSFER name1 name2 sum - перевести сумму sum со счета клиента name1
# на счет клиента name2. Если у какого-либо клиента нет счета, то ему
# создается счет.
#
# INCOME p - начислить всем клиентам, у которых открыты счета, p% от
# суммы счета. Проценты начисляются только клиентам с положительным
# остатком на счету, если у клиента остаток отрицательный, то его счет
# не меняется. После начисления процентов сумма на счету остается
# целой, то есть начисляется только целое число денежных единиц.
# Дробная часть начисленных процентов отбрасывается.
#
# Формат вывода
# Для каждого запроса BALANCE программа должна вывести остаток на счету
# данного клиента. Если же у клиента с запрашиваемым именем не открыт
# счет в банке, выведите ERROR.

bal = {}
with open("input.txt") as f:
    for line in f:
        cmd = line.split()
        if cmd[0] == "DEPOSIT":
            bal[cmd[1]] = bal.get(cmd[1], 0) + int(cmd[2])
        if cmd[0] == "WITHDRAW":
            bal[cmd[1]] = bal.get(cmd[1], 0) - int(cmd[2])
        if cmd[0] == "BALANCE":
            print(bal[cmd[1]] if cmd[1] in bal else "ERROR")
        if cmd[0] == "TRANSFER":
            bal[cmd[1]] = bal.get(cmd[1], 0) - int(cmd[3])
            bal[cmd[2]] = bal.get(cmd[2], 0) + int(cmd[3])
        if cmd[0] == "INCOME":
            for k, v in bal.items():
                if v > 0:
                    bal[k] = int(bal.get(k) * (1 + int(cmd[1]) / 100))


# bank = dict()
#
#
# def deposit(name_and_sum, sign=1):
#     name, summ = name_and_sum.split()
#     bank[name] = bank.get(name, 0) + int(summ) * sign
#
#
# def withdraw(name_and_sum):
#     deposit(name_and_sum, sign=-1)
#
#
# def balance(name):
#     print(bank.get(name, 'ERROR'))
#
#
# def transfer(name_and_sum):
#     withdraw(' '.join(name_and_sum.split()[::2]))
#     deposit(' '.join(name_and_sum.split()[1:]))
#
#
# def income(prs):
#     for name, summ in bank.items():
#         bank[name] = int(summ * (1 + int(prs) / 100 * (summ > 0)))
#
#
# commands = dict(DEPOSIT=deposit, WITHDRAW=withdraw, BALANCE=balance,
#                 TRANSFER=transfer, INCOME=income)
#
# with open('input.txt', encoding='utf8') as inf:
#     for line in inf:
#         command, name_and_sum = line.strip().split(' ', 1)
#         action = commands.get(command)
#         action(name_and_sum)
