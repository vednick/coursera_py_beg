"""Телефонные номера в адресной книге мобильного телефона имеют один
из следующих форматов:

+7<код><номер>
8<код><номер>
<номер>

где <номер> — это семь цифр, а <код> — это три цифры или три цифры в
круглых скобках. Если код не указан, то считается, что он равен 495.
Кроме того, в записи телефонного номера может стоять знак “-” между
любыми двумя цифрами (см. пример). На данный момент в адресной книге
телефона Васи записано всего три телефонных номера, и он хочет записать
туда еще один. Но он не может понять, не записан ли уже такой номер в
телефонной книге. Помогите ему! Два телефонных номера совпадают, если у
них равны коды и равны номера. Например, +7(916)0123456 и 89160123456 —
это один и тот же номер.

Формат ввода
В первой строке входных данных записан номер телефона, который Вася
хочет добавить в адресную книгу своего телефона. В следующих трех
строках записаны три номера телефонов, которые уже находятся в адресной
книге телефона Васи. Гарантируется, что каждая из записей соответствует
одному из трех приведенных в условии форматов.

Формат вывода
Для каждого телефонного номера в адресной книге выведите YES, если он
совпадает с тем телефонным номером,который Вася хочет добавить в адресную
книгу или NO в противном случае.
"""


ph = {}
with open("phones.txt") as f:
    for i, line in enumerate(f):
        for j in line.strip():
            if j.isdigit():
                ph[i] = ph.get(i, "") + j
        ph[i] = "495" + ph[i] if len(ph[i]) < 10 else ph[i][-10:]
for i in range(1, len(ph)):
    print("YES" if ph[i] == ph[0] else "NO")


# A = []
# for i in range(4):
#     l = input()
#     A.append(''.join([s for s in l if s.isdigit()]))
#     A[i] = A[i][1:] if len(A[i]) == 11 else '495' + A[i]
#     if i != 0:
#         print('YES') if A[0] == A[i] else print('NO')


# def dig(string):
#     res = ''.join(list(filter(str.isdigit, str(string.replace('+7', '8')))))
#     if len(res) < 11:
#         res = '8495' + res
#     return res
#
#
# with open('input.txt', 'r', encoding='utf8') as inFile:
#     new_numb = dig(inFile.readline())
#     numb = list(map(dig, inFile.readlines()))
# for _ in numb:
#     print('YES' if new_numb == _ else 'NO')


# n_l = []
# for i in range(4):
#     n_l.append(''.join([j for j in input() if j.isdigit()]))
#     n_l[i] = "8495" + n_l[i] if len(n_l[i]) == 7 else n_l[i]
# [print(["NO", "YES"][n_l[0][1:] == n_l[i][1:]]) for i in range(1, 4)]