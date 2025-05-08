# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N) заполняется случайным образом
# целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное,
# введенное из файла или полученное генератором. Условно матрица разделена на 4 части.
# Формируется матрица F следующим образом: Скопировать в нее матрицу А и если минимальный элемент в нечетных столбцах
# в области 1 меньше, чем сумма чисел в нечетных строках в области 3, то поменять симметрично области 3 и 2 местами,
# иначе 2 и 3 поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение:
# (К*F)*А– K*AT . Выводятся по мере формирования А, F и все матричные операции последовательно.
# ИСТбд-11, Хасанов Кирилл, Вариант 15

def read_matrix(filename):
    with open(filename, "r") as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

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

F = [row[:] for row in A]

# Минимальный элемент в нечетных столбцах области 1
min_val = float('inf')
for i in range(N // 2):
    for j in range(i):
        if j % 2 != 0:
            min_val = min(min_val, F[i][j])

for i in range(N // 2, N):
    for j in range(N - i - 1):
        if j % 2 != 0:
            min_val = min(min_val, F[i][j])

# Сумма элементов в нечетных строках области 3
sum_val = 0
for i in range(1, N // 2):
    for j in range(N - i, N):
        if i % 2 != 0:
            sum_val += F[i][j]

for i in range(N // 2, N):
    for j in range(i + 1, N):
        if i % 2 != 0:
            sum_val += F[i][j]

if min_val < sum_val:
    print("min < sum. Перестановка симметрично областей 3 и 2.")
    for i in range(N // 2):
        for j in range(N):
            if (i < j) and (i < N - j):
                tmp = F[i][j]
                F[i][j] = F[N - 1 - j][N - 1 - i]
                F[N - 1 - j][N - 1 - i] = tmp
else:
    print("min >= sum. Перестановка несимметрично областей 2 и 3.")
    for i in range(N // 2):
        for j in range(N):
            if (i < j) and (i < N - j):
                tmp = F[i][j]
                F[i][j] = F[j][N - 1 - i]
                F[j][N - 1 - i] = tmp

print_matrix("Матрица F", F)

#K * F
kf = [[K * F[i][j] for j in range(N)] for i in range(N)]
print_matrix("K * F", kf)

#(K * F) * A
kf_a = [[sum(kf[i][m] * A[m][j] for m in range(N)) for j in range(N)] for i in range(N)]
print_matrix("(K * F) * A", kf_a)

#A^T
a_t = [[A[j][i] for j in range(N)] for i in range(N)]
print_matrix("A^T", a_t)

#K * A^T
ka_t = [[K * a_t[i][j] for j in range(N)] for i in range(N)]
print_matrix("K * A^T", ka_t)

#(K*F)*A - K*A^T
result = [[kf_a[i][j] - ka_t[i][j] for j in range(N)] for i in range(N)]
print_matrix("(K*F)*A - K*A^T", result)