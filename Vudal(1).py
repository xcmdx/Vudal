N, K = map(int, input().split())#N - кол-во строк, K- кол-во столбцов
mas = [[0 for i in range(1, K + 1)] for j in range(1, N + 1)] 
"""
for k in range(1, K + 2):
    for n in range(1, N + 2):
        if n + 2 <= k:
            mas[k][n] = 0
        else:
            mas[k][n] = n * k ** n - 1
mas[N + 1][K + 1] = 0
"""
mas[1 - 1][2 - 1] = 1
print(mas)