"""
Всем известно, что со временем клавиатура изнашивается, и клавиши на ней
начинают залипать. Конечно, некоторое время такую клавиатуру еще можно
использовать, но для нажатий клавиш приходиться использовать большую силу.

При изготовлении клавиатуры изначально для каждой клавиши задается количество
нажатий, которое она должна выдерживать. Если знать эти величины для
используемой клавиатуры, то для определенной последовательности нажатых
клавиш можно определить, какие клавиши в процессе их использования сломаются,
а какие — нет.

Требуется написать программу, определяющую, какие клавиши сломаются в процессе
заданного варианта эксплуатации клавиатуры.

Формат ввода
Первая строка входных данных содержит целое число n (1≤n≤1000) — количество
клавиш на клавиатуре. Вторая строка содержит n целых чисел —с₁, с₂, … , сn,
где сᵢ (1≤cᵢ≤100000) — количество нажатий,выдерживаемых i-ой клавишей. Третья
строка содержит целое число k (1≤k≤100000) — общее количество нажатий клавиш,
и последняя строка содержит k целых чисел pj (1≤pj≤n) — последовательность
нажатых клавиш.

Формат вывода
Программа должна вывести n строк, содержащих информацию об исправности клавиш.
Если i-я клавиша сломалась, то i-ая строка должна содержать слово YES, если же
клавиша работоспособна — слово NO.
"""


# key_num = int(input())
# press_limit = [int(i) for i in input().split()]
# press_total = int(input())
# queue_press = [int(i) for i in input().split()]
#
# # count the number of times each key was pressed
# keystrokes = [0] * key_num
# for key in queue_press:
#     keystrokes[key - 1] += 1
#
# # compare limits and keystrokes
# for i, key in enumerate(keystrokes):
#     print("YES" if key > press_limit[i] else "NO")


key_num = int(input())
press_limit = [int(i) for i in input().split()]
press_total = int(input())
queue_press = [int(i) for i in input().split()]

# compare the number of times each key was pressed with limits
for key in queue_press:
    press_limit[key - 1] -= 1

# check limits
for i in press_limit:
    print("YES" if i < 0 else "NO")