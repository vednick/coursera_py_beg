# Дана база данных о продажах некоторого интернет-магазина. Каждая
# строка входного файла представляет собой запись вида
#
# Покупатель товар количество, где
#
# Покупатель — имя покупателя (строка без пробелов),
# товар — название товара (строка без пробелов),
# количество — количество приобретенных единиц товара.
#
# Создайте список всех покупателей, а для каждого покупателя
# подсчитайте количество приобретенных им единиц каждого вида товаров.
#
# Формат ввода
# Вводятся сведения о покупках в указанном формате.
#
# Формат вывода
# Выведите список всех покупателей в лексикографическом порядке,после
# имени каждого покупателя выведите двоеточие, затем выведите список
# названий всех приобретенных данным покупателем товаров в
# лексикографическом порядке, после названия каждого товара выведите
# количество единиц товара, приобретенных данным покупателем.Информация
# о каждом товаре выводится в отдельной строке.


sales = {}
with open("input.txt", "r", encoding="utf8") as f:
    for line in f:
        name, goods, amount = line.split()
        amount = int(amount)
        if name in sales:
            if goods in sales[name]:
                sales[name][goods] += amount
            else:
                sales[name].update({goods: amount})
        else:
            sales[name] = {goods: amount}
for k, v in sorted(sales.items()):
    print(k + ":", *[" ".join(map(str, (g, a))) for
                     g, a in sorted(v.items())], sep="\n")


# d = {}
# with open('input.txt') as in_file:
#     for f in in_file:
#         name, item, amount = f.split()
#         d[name] = d.get(name, dict())
#         d[name][item] = d[name].get(item, 0) + int(amount)
# for name in sorted(d):
#     print(name, ':', sep='')
#     [print(item, d[name][item]) for item in sorted(d[name])]
