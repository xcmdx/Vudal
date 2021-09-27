N, K = map(int, input().split())
mas = [[0 for i in range(1, N + 2)] for j in range(1, K + 2)] #n - кол-во чтолбцов, k- кол-во строк
for n in range(1, N + 2):
    for k in range(1, K + 2):
        if n + 2 <= k:
            mas[n][k] = 0
        else:
            mas[n][k] = n * k ** n - 1
mas[N + 1][K + 1] = 0
print(mas)