N, K = map(int, input().split())#N - кол-во строк, K- кол-во столбцов
mas = [[0 for i in range(1, K + 3)] for j in range(1, N + 3)] 

mas[0][0] = 1
for j in range(1, N + 2):
    for i in range(1, K + 2):
        print(mas[j][i], end = ' ')
        if i == K + 1:
            print()
print(mas)