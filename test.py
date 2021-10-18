"""
Потехин Павел Михайлович
15 вариант
КИ21-17/2б
"""
TEXT_MESSAGE_1 = 'Нажмите 1 + Enter, чтобы создать новую таблицу чисел Вудала'
TEXT_MESSAGE_2 = 'Нажмите 2 + Enter, чтобы найти сумму чисел в строках'
TEXT_MESSAGE_3 = 'Нажмите 3 + Enter, чтобы найти сумму чисел в столбцах'
TEXT_MESSAGE_4 = 'Нажмите 4 + Enter, чтобы получить дополненную таблицу Вудала'
TEXT_MESSAGE_5 = 'Нажмите 5 + Enter, чтобы выйти из программы'
Error_1 = '!!! ВВЕДЕНА НЕСУЩЕСТВУЮЩАЯ КОМАНДА, ПОВТОРИТЕ ПОПЫТКУ !!!'
Error_2 = '!!! НЕПРАВИЛЬНО ВВЕДЕНЫ ЧИСЛА, ПОВТОРИТЕ ПОПЫТКУ !!!'


def good(var, N, K):
    try:
        N = int(N)
        K = int(K)
    except ValueError:
        print('\n', Error_2, '\n')
        return -1, -1
    if N < 0 or K < 0:
        print('\n', Error_2, '\n')
        return -1, -1
    if var == 1:
        a, b, c = Vudal(N, K)
        vtorostepennaya(a, b, c)
    elif var == 2:
        a, b, c = Vudal(N, K)
        a, b, c = sum_of_lines(a, b, c)
        vtorostepennaya(a, b, c)
    elif var == 3:
        a, b, c = Vudal(N, K)
        a, b, c = sum_of_columns(a, b, c)
        vtorostepennaya(a, b, c)
    elif var == 4:
        a, b, c = Vudal(N, K)
        a, b, c = sum_of_columns(a, b, c)
        a, b, c = sum_of_lines(a, b, c)
        mas = a
        mas[b - 1][c - 1] = 0
        vtorostepennaya(mas, b, c)
    string = input('Введите 1, чтобы вернуться в Меню: ')
    while check(string) != 1:
        print(Error_1)
        string = input('Введите 1, чтобы вернуться в Меню: ')
    return N, K


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
    return mas, N, K + 1


def sum_of_columns(mas, N, K):  # выводит сумму чисел в столбцах
    string = [0 for _ in range(K)]
    mas.append(string)
    for n in range(N + 1):
        for k in range(K):
            if n == N:
                for column in range(N):
                    mas[n][k] += mas[column][k]
    return mas, N + 1, K


def check(string):
    try:
        string = int(string)
    except ValueError:
        print('\n',
              Error_1,
              '\n')
    return string


def menu():
    start = 0
    while (start != 2):
        N = -1
        K = -1
        start = input(
            'Введите 1, чтобы создать таблицу Вудала или 2, чтобы выйти из программы: ')
        start = check(start)
        while (start != 1) + (start != 2) - 1 > 0:
            print(Error_1)
            start = input(
                'Введите 1, чтобы создать таблицу Вудала или 2, чтобы выйти из программы: ')
            start = check(start)
        if start == 1:
            while (N == -1) and (K == -1):
                N = input('Количество строк:')
                K = input('Количество столбцов:')
                N, K = good(1, N, K)
        while True:
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
                break
            elif var == 2:
                good(var, N, K)
            elif var == 3:
                good(var, N, K)
            elif var == 4:
                good(var, N, K)
            elif var == 5:
                return False
            else:
                print('\n', Error_1, '\n')


menu()
