"""
Потехин Павел Михайлович
15 вариант
КИ21-17/2б
"""
TEXT_MESSAGE_1 = 'Нажмите 1 + Enter, чтобы создать таблицу чисел Вудала'
TEXT_MESSAGE_2 = 'Нажмите 2 + Enter, чтобы найти сумму чисел в строках'
TEXT_MESSAGE_3 = 'Нажмите 3 + Enter, чтобы найти сумму чисел в столбцах'
TEXT_MESSAGE_4 = 'Нажмите 4 + Enter, чтобы получить дополненную таблицу Вудала'
TEXT_MESSAGE_5 = 'Нажмите 5 + Enter, чтобы выйти из программы'
Error_1 = '!!! ВВЕДЕНА НЕСУЩЕСТВУЮЩАЯ КОМАНДА, ПОВТОРИТЕ ПОПЫТКУ !!!'
Error_2 = '!!! НЕПРАВИЛЬНО ВВЕДЕНЫ ЧИСЛА, ПОВТОРИТЕ ПОПЫТКУ !!!'


def good_1(N, K):
    try:
        N = int(N)
        K = int(K)
    except ValueError:
        print('\n', Error_2, '\n')
        return True
    a, b, c = Vudal(N, K)
    vtorostepennaya(a, b, c)


def good_2(N, K):
    try:
        N = int(N)
        K = int(K)
    except ValueError:
        print('\n', Error_2, '\n')
        return True
    a, b, c = Vudal(N, K)
    sum_of_lines(a, b, c)


def good_3(N, K):
    try:
        N = int(N)
        K = int(K)
    except ValueError:
        print('\n', Error_2, '\n')
        return True
    a, b, c = Vudal(N, K)
    sum_of_columns(a, b, c)


def good_4(N, K):
    try:
        N = int(N)
        K = int(K)
    except ValueError:
        print('\n', Error_2, '\n')
        return True
    full(N, K)

def Vudal(N, K):  # таблица Вудала
    # N- кол-во строк, K - кол-во столбцов
    mas = [[0 for _ in range(K)] for _ in range(N)]
    for n in range(N):
        for k in range(K):
            if (n + 2 > k):
                mas[n][k] = (n + 1) * (k + 1) ** (n + 1) - 1
            else:
                mas[n][k] = 0
    return mas, N, K


def vtorostepennaya(mas, N, K):  # выводит таблицу Вудала без дополнений
    for n in range(N):
        for k in range(K):
            print(mas[n][k], end=' ')
            if k == K - 1:
                print()


def sum_of_lines(mas, N, K):  # выводит сумму чисел в строке
    for n in range(N):
        mas[n].append(0)
        sum_n = 0
        for k in range(K + 1):
            if k != K:
                sum_n += mas[n][k]
            else:
                mas[n][k] = sum_n
            print(mas[n][k], end=' ')
            if k == K:
                print()


def sum_of_columns(mas, N, K):  # выводит сумму чисел в столбцах
    string = [0 for _ in range(K)]
    mas.append(string)
    for n in range(N + 1):
        for k in range(K):
            if n == N:
                for column in range(N):
                    mas[n][k] += mas[column][k]
            print(mas[n][k], end=' ')
            if k == K - 1:
                print()


def full(N, K):
    mas = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    for n in range(N + 1):
        sum_n = 0  # сумма элементов строки
        for k in range(K + 1):
            if n != N:
                if (n + 2 > k) & (k != K):
                    mas[n][k] = (n + 1) * (k + 1) ** (n + 1) - 1
                    sum_n += mas[n][k]
                elif (k == K):
                    mas[n][k] = sum_n
                else:
                    mas[n][k] = 0
            else:
                for column in range(N):  # сумма элементов столбца
                    mas[n][k] += mas[column][k]
                mas[N][K] = 0
            print(mas[n][k], end=' ')
            if k == K:
                print()


def check(string):
    try:
        string = int(string)
    except ValueError:
        print('\n',
            Error_1,
            '\n')
    return string

    
def menu():
    print(
        '\n' +
        '*** МЕНЮ ***' +
        '\n' +
        TEXT_MESSAGE_1 +
        '\n' +
        TEXT_MESSAGE_2 +
        '\n' +
        TEXT_MESSAGE_3 +
        '\n' +
        TEXT_MESSAGE_4 +
        '\n' + 
        TEXT_MESSAGE_5 +
        '\n')
    var = input()
    var = check(var)
    if var == 1:
        N = input('Количество строк:')
        K = input('Количество столбцов:')
        good_1(N, K)
        string = input('Введите 1, чтобы вернуться в Меню: ')
        while check(string) != 1:
            string = input('Введите 1, чтобы вернуться в Меню: ')
        return True
    elif var == 2:
        N = input('Количество строк:')
        K = input('Количество столбцов:')
        good_2(N, K)
        string = input('Введите 1, чтобы вернуться в Меню: ')
        while check(string) != 1:
            string = input('Введите 1, чтобы вернуться в Меню: ')
        return True
    elif var == 3:
        N = input('Количество строк:')
        K = input('Количество столбцов:')
        good_3(N, K)
        string = input('Введите 1, чтобы вернуться в Меню: ')
        while check(string) != 1:
            string = input('Введите 1, чтобы вернуться в Меню: ')
        return True
    elif var == 5:
        return False
    else:
        print(
        '\n',
        Error_1,
        '\n')
        return True


while menu():
    pass

