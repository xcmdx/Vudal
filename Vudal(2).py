"""
Потехин Павел Михайлович
15 вариант
КИ21-17/2б
"""


N, K = map(int, input().split())  
print('Таблица чисел Вудала')
mas = [[0 for i in range(K + 1)] for j in range(N + 1)]  # N- кол-во строк, K - кол-во столбцов
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
            for d in range(N):  # сумма элементов столбца
                mas[n][k] += mas[d][k]
            mas[N][K] = 0
        print(mas[n][k], end=' ')
        if k == K:
            print()


def function():
    if K == '' or N == '':
        return False
    