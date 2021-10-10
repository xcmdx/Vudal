N, K = map(int, input().split())
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