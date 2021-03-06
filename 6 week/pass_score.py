"""
Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов
в виде ЕГЭ, каждый из них оценивается целым числом от 0 до 100 баллов.
При этом абитуриенты, набравшие менее 40 баллов (неудовлетворительную оценку)
по любому экзамену из конкурса выбывают. Остальные абитуриенты участвуют
в конкурсе по сумме баллов за три экзамена.

В конкурсе участвует N человек, при этом количество мест равно K. Определите
проходной балл, то есть такое количество баллов, что количество участников,
набравших столько или больше баллов не превосходит K, а при добавлении к ним
абитуриентов, набравших наибольшее количество баллов среди непринятых
абитуриентов, общее число принятых абитуриентов станет больше K.

Формат ввода
Программа получает на вход количество мест K. Далее идут строки с информацией
об абитуриентах, каждая из которых состоит из имени (текстовая строка
содержащая произвольное число пробелов) и трех чисел от 0 до 100,
разделенных пробелами.

Используйте для ввода файл input.txt с указанием кодировки utf8 (для создания
такого файла на своем компьютере в программе Notepad++ следует использовать
кодировку UTF-8 без BOM).

Формат вывода
Программа должна вывести проходной балл в конкурсе. Выведенное значение должно
быть минимальным баллом, который набрал абитуриент, прошедший по конкурсу.

Также возможны две ситуации, когда проходной балл не определен.

Если будут зачислены все абитуриенты, не имеющие неудовлетворительных оценок,
программа должна вывести число 0.

Если количество имеющих равный максимальный балл абитуриентов больше чем K,
программа должна вывести число 1.

Используйте для вывода файл output.txt с указанием кодировки utf8.

Предупреждение
Пожалуйста, тестируйте файловый ввод и вывод на своем компьютере. В этой
задаче слушатели часто получают ошибки вроде RE на первом тесте, протестировав
у себя с помощью консоли и просто заменив input() на чтение из файла перед
сдачей. К сожалению, такую замену не всегда удается сделать без ошибок,
и решение слушателей действительно перестает правильно работать даже на
первом тесте.
"""

enr_short = []
with open("pass_score.txt", "r", encoding="utf8") as f:
    k = int(f.readline().strip())
    for line in f:
        en_tmp = [int(i) for i in line.split()[-3:]]
        if min(en_tmp) >= 40:
            enr_short.append(sum(en_tmp))

# enr_short.sort(reverse=True)
# with open("output.txt", "w", encoding="utf8") as fo:
#     if len(enr_short) <= k:
#         print(0, file=fo)
#     elif sum(enr_short[:k + 1]) / (k + 1) == enr_short[0]:
#         print(1, file=fo)
#     else:
#         if enr_short[k - 1] != enr_short[k]:
#             print(enr_short[k - 1], file=fo)
#         else:
#             while enr_short[k - 1] == enr_short[k - 2]:
#                 k -= 1
#             print(enr_short[k - 2], file=fo)

with open("output.txt", "w", encoding="utf8") as fo:
    if len(enr_short) <= k:
        print(0, file=fo)
    else:
        enr_short.sort(reverse=True)
        a = 1
        for i in enr_short[:k + 1]:
            if i > enr_short[k]:
                a = i
        print(a, file=fo)
