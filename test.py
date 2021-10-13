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


def check(string):
    try:
        string = int(string)
    except ValueError:
        print('\n',
            "Error_1",
            '\n')
    return string


while True:
