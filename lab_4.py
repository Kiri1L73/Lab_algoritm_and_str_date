#С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E
#заполняется случайным образом целыми числами в интервале [-10,10]. Для отладки использовать не случайное заполнение,
#а целенаправленное (ввод из файла и генератором).
#Вид матрицы А:
#B  C
#D  E
#На основе матрицы А формируется матрица F. По матрице F необходимо вывести не менее 3 разных графика.
#Программа должна использовать функции библиотек numpy  и matplotlib/
#Формируется матрица F следующим образом: скопировать в нее А и  если в Е количество чисел, больших К в четных столбцах больше,
#чем сумма чисел в нечетных строках, то поменять местами С и Е симметрично, иначе В и С поменять местами несимметрично.
#При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
#то вычисляется выражение: A*AT – K * FТ, иначе вычисляется выражение (AТ +G^-1-F^-1)*K, где G-нижняя треугольная матрица,
#полученная из А. Выводятся по мере формирования А, F и все матричные операции последовательно.
#ИСТбд-11, Хасанов Кирилл, вариант №15

import numpy as np
import matplotlib.pyplot as plt
import random

sum = kol = diag_F = 0

def read_matrix(filename):
    with open(filename, "r") as file:
        matrix = [list(map(int, line.split())) for line in file]
    return np.array(matrix)

def print_matrix(name, m):
    print(f"{name}:")
    for row in m:
        print(row)
    print()

K = int(input("Введите значение K: "))
N = int(input("Введите размерность матрицы N: "))

filename = "matrix.txt"

A = read_matrix(filename)
print_matrix("Матрица А", A)

F = np.array([row[:] for row in A])

for i in range(N // 2, N):
    for j in range(N // 2, N):
        if j % 2 == 0 and F[i][j] > K:
            kol += 1
print("Количество чисел, больших К в четных столбцах: ", kol)

for i in range(N // 2, N):
    for j in range(N // 2, N):
        if i % 2 != 0:
            sum += F[i][j]
print("Сумма чисел в нечетных строках: ", sum)

if (kol > sum):
    for i in range(N // 2):
        for j in range(N // 2, N):
            F[i][j], F[N - 1 - i][j] = F[N - 1 - i][j], F[i][j] # Замена С и Е симметрично
else:
    for i in range(N // 2):
        for j in range(N // 2):
            F[i][j], F[i][j + N // 2] = F[i][j + N // 2], F[i][j] # Замена В и С несимметрично

print_matrix("Матрица F", F)

# Вычисление нижней треугольной матрицы G
G = [[random.randint(0,0) for i in range(N)] for j in range(N)]
for i in range(N // 2 + 1, N):
    for j in range(N - i, i):
        G[i][j] = int(A[i][j])
print_matrix("Нижняя треугольная матрица G", G)

sum_diag_F = np.trace(F)
det_A = np.linalg.det(A)

print("Определитель матрицы A:", det_A)
print("Сумма диагональных элементов F:", sum_diag_F)

if (det_A > sum_diag_F):
    print("det_A > sum_diag_F. Вычисление A * A.T - K * F.T")
    A_tr=[[A[j][i] for j in range(N)] for i in range(N)]
    F_tr = [[F[j][i] for j in range(N)] for i in range(N)]
    A_np = np.array(A)
    F_np = np.array(F)
    A_tr_np = np.array(A_tr)
    F_tr_np = np.array(F_tr)
    result = np.matmul(A_np, A_tr_np) - np.matmul(K * F_tr_np)
    result_r = np.round(result)
else:
    print("det_A < sum_diag_F. Вычисление A.T + G⁻¹ - F⁻¹")
    A_tr=[[A[j][i] for j in range(N)] for i in range(N)]
    F_tr=[[F[j][i] for j in range(N)] for i in range(N)]
    G = [[random.randint(0,0) for i in range(N)] for j in range(N)]
    for i in range(N // 2 + 1, N):
        for j in range(N - i, i):
            G[i][j] = A[i][j]
    F_np = np.array(F)
    G_np = np.array(G)
    A_tr_np = np.array(A_tr)
    F_tr_np = np.array(F_tr)
    result = (A_tr_np + np.linalg.pinv(G_np) - np.linalg.pinv(F_np)) * K
    result_r = np.round(result)
print("\nВычисление по формуле: \n")
for A in result_r:
    print(A)

plt.figure(figsize=(N, N))

plt.subplot(1, 3, 1)
plt.imshow(F, cmap='coolwarm')

plt.subplot(1, 3, 2)
row_means = np.mean(F, axis=1)
plt.plot(row_means, marker='o', color='red')

plt.subplot(1, 3, 3)
plt.hist(F_np.flatten(), bins=N, color='green', edgecolor='black')

plt.tight_layout()
plt.show()