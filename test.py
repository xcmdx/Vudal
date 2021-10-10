def sum_of_lines(mas, N, K):
    for n in range(N):
        for k in range(K + 1):
            if k == K:
                mas.append(mas[n][k])
    print(mas)
#    for n in range(N):
#        sum_n = 0
#        for k in range(K + 1):
#            if n != N - 1:
#                if k != K:
#                    mas[n][k] = (n + 1) * (k + 1) ** (n + 1) - 1
#                    sum_n += mas[n][k]
#                else:
#                    mas[n][k] = sum_n
#            print(mas[n][k], end=' ')
#            if k == K:
#                print()