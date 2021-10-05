"""
Потехин Павел Михайлович
15 вариант
КИ21-17/2б
"""
TEXT_MESSAGE_1 = 'Нажмите 1 + Enter, чтобы создать таблицу чисел Вудала'
TEXT_MESSAGE_2 = 'Нажмите 2 + Enter, чтобы посмотреть условие задачи'
TEXT_MESSAGE_3 = 'Нажмите 3 + Enter, чтобы выйти из программы'


def Vudal(N, K):
    print('Таблица чисел Вудала')
    # N- кол-во строк, K - кол-во столбцов
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


def good(N, K):
    try:
        N = int(N)
        K = int(K)
    except ValueError:
        print('\n', '!!! НЕПРАВИЛЬНО ВВЕДЕНЫ ЧИСЛА, ПОВТОРИТЕ ПОПЫТКУ !!!', '\n')
        return True
    Vudal(N, K)
    return True


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
        '\n')
    var = input()
    try:
        var = int(var)
    except ValueError:
        print(
            '\n',
            '!!! ВВЕДЕНА НЕСУЩЕСТВУЮЩАЯ КОМАНДА, ПОВТОРИТЕ ПОПЫТКУ !!!',
            '\n')
        return True
    if var == 1:
        N = input('Количество строк:')
        K = input('Количество столбцов:')
        good(N, K)
        return input('Введите букву(ы) или цифру(ы), чтобы вернуться в меню: ')
    elif var == 2:
        print('*** УСЛОВИЕ ЗАДАЧИ ***')
        print(
            'Сгенерировать двумерный массив размером N * K и заполнить его числами Вудала:')
        print('𝑥(𝑛)(𝑘) = 𝑛𝑘^𝑛 − 1, 𝑛 + 2 > 𝑘, 1 ≤ k ≤ K, 1 ≤ n ≤ N.')
        print('Добавить в матрицу строку N + 1 и записать туда сумму чисел из столбцов.')
        print('Добавить в матрицу столбец K + 1 и записать туда сумму чисел из строк.')
        print('Ячейку с индексами [N + 1, K + 1] оставить равной 0.')
        print('Ячейки, где условие 𝑛 + 2 > 𝑘 не выполнится заполнить 0.')
        return input('Введите букву(ы) или цифру(ы), чтобы вернуться в меню: ')
    elif var == 3:
        return False
    else:
        print(
            '\n',
            '!!! ВВЕДЕНА НЕСУЩЕСТВУЮЩАЯ КОМАНДА, ПОВТОРИТЕ ПОПЫТКУ !!!',
            '\n')
        return True


while menu():
    pass


