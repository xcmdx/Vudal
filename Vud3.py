def Vudal(N, K):
    print('Таблица чисел Вудала')
    # N- кол-во строк, K - кол-во столбцов
    mas = [[0 for _ in range(K)] for _ in range(N)]
    for n in range(N):
        for k in range(K):
            if (n + 2 > k):
                mas[n][k] = (n + 1) * (k + 1) ** (n + 1) - 1
            else:
                mas[n][k] = 0
            print(mas[n][k], end=' ')
            if k == K - 1:
                print()
    return mas, N, K 

a, b, c = Vudal(3, 4)
a = list(a)
b, c = int(b), int(c)


def sum_of_columns(mas, N, K):
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

#print(sum_of_columns(a, b, c))


def sum_of_lines(mas, N, K):
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


print(sum_of_lines(a, b, c))