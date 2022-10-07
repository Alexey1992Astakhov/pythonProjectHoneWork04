#4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.
#in
#9
#5
#3

#out in the file
#3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
#4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
#4*x^2 - 4 = 0

#in
#0
#-1
#4
#out in the file
#3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
#4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
#4*x^2 - 4 = 0
#2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

from random import randint

print('Введите натуральную степень k:')
k = int(input())


def write_file(st):
    with open('Task04.txt', 'w') as data:
        data.write(st)


def create_list(k):
    list = []
    for i in range(k + 1):
        list.append(randint(0, 11))
    return list


def create_str(sp):
    list = sp[::-1]
    wr = ''
    if len(list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                wr += f'{list[i]}x^{len(list) - i - 1}'
                if list[i + 1] != 0:
                    wr += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                wr += f'{list[i]}x'
                if list[i + 1] != 0:
                    wr += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                wr += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                wr += ' = 0'
    return wr


koef = create_list(k)
write_file(create_str(koef))