"""
Известно, что фамилии всех участников — различны. Сохраните в массивах
список всех участников и выведите его, отсортировав по фамилии в
лексикографическом порядке. При выводе указываете фамилию, имя участника
и его балл.

Используйте для ввода и вывода файлы input.txt и output.txt с указанием
кодировки utf8. Например, для чтения откройте файл с помощью open('input.txt',
'r', encoding='utf8').

Входные данные
Строки вида "Фамилия Имя НомерШколы Балл".

Выходные данные
Строки вида "Фамилия Имя Балл", отсортированные по фамилии.

Примечание
Если у Вас Wrong Answer на первом тесте и в вердикте в качестве правильного
ответа показываются знаки вопросов, это не значит, что их действительно нужно
выводить. Это баг Курсеры – в вердикте кириллица не поддерживается. Курсера
знает о проблеме с 25.10.2018 и возможно починит.

В итоге, при WA на первом тесте не стоит смотреть на вердикт, нужно искать
ошибку в решении.
"""


from collections import namedtuple as nt

# with open('list_sort.txt', 'r', encoding='utf8') as f:
#     Student = nt('Student', 'sn, n, sch, sc')
#     st_arr = []
#     for line in f:
#         s_tmp = line.split()
#         st = Student(sn=s_tmp[0], n=s_tmp[1], sch=s_tmp[2], sc=s_tmp[3])
#         st_arr.append(st)
#     st_arr.sort()
#     for i in st_arr:
#         print(i.sn, i.n, i.sc)


with open('list_sort.txt', 'r', encoding='utf8') as f:
    Student = nt('Student', 'sn, n, sch, sc')
    st_arr = []
    for line in f:
        s_tmp = line.split()
        st = Student(sn=s_tmp[0], n=s_tmp[1], sch=s_tmp[2], sc=s_tmp[3])
        st_arr.append(st)
    st_arr.sort()
with open("output.txt", "w", encoding="utf8") as fo:
    for i in st_arr:
        print(i.sn, i.n, i.sc, file=fo)

# with open('input.txt', 'r', encoding='utf8') as f:
#     st_arr = []
#     for line in f:
#         st_arr.append((line.split()))
#     st_arr.sort()
#     for i in st_arr:
#         print(i[0], i[1], i[3])


# with open('input.txt', 'r', encoding='utf8') as f:
#     st_arr = []
#     for line in f:
#         st_arr.append((line.split()))
#     st_arr.sort()
# with open("output.txt", "w", encoding="utf8") as fo:
#     for i in st_arr:
#         fo.write(i[0] + " " + i[1] + " " + i[3] + "\n")
