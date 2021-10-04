N, K = map(int, input().split())#N - кол-во строк, K- кол-во столбцов
mas = [[0 for i in range(1, K + 2)] for j in range(1, N + 2)] 


for j in range(N + 1):
    for i in range(K + 1):
        print(mas[j][i], end = ' ')
        if i == K:
            print()
