import timeit
import math
import matplotlib.pyplot as plt

n = int(input("Введите число n: "))


def fact(k):
    if k == 1:
        return 1
    else:
        return k * fact(k - 1)


def recursive(n, memo={0: 1, 1: 1}):
    if n not in memo:
        factorial_n = fact(n)
        memo[n] = (-1 if n % 2 else 1) * (2 * recursive(n - 1, memo) / factorial_n + recursive(n - 2, memo))
    return memo[n]


def iterative(n):
    if n == 0 or n == 1:
        return 1
    znach_1 = 1  # F(0)
    znach_2 = 1  # F(1)
    for i in range(2, n + 1):
        factorial_n = math.factorial(i)
        last = (-1 if i % 2 else 1) * (2 * znach_2 / factorial_n + znach_1)
        znach_1 = znach_2
        znach_2 = last
    return last


def time_it(func, n):
    return timeit.timeit(lambda: func(n), number=1)


def sravnenie(n):
    print(f"{'n':>3} | {'Rec (s)':>10} | {'Iter (s)':>10} | {'F_rec(n)':>14} | {'F_iter(n)':>10}")
    print('-' * 62)

    rec_times = []
    iter_times = []

    for i in range(0, n + 1):
        # Рекурсивное вычисление
        try:
            rec_result = recursive(i)
            rec_time = time_it(recursive, i)
        except RecursionError:
            rec_result = 'RecursionError'
            rec_time = float('inf')  # Задаем бесконечное время для рекурсии при ошибке

        # Итеративное вычисление
        iter_result = iterative(i)
        iter_time = time_it(iterative, i)

        znachenie_rec = f"{rec_result:.10f}" if isinstance(rec_result, (float, int)) else str(rec_result)
        znachenie_iter = f"{iter_result:.10f}" if isinstance(iter_result, (float, int)) else str(iter_result)

        print(f"{i:>3} | {rec_time:>10.6f} | {iter_time:>10.6f} | {znachenie_rec:>14} | {znachenie_iter:>10}")

        rec_times.append(rec_time)
        iter_times.append(iter_time)

    plt.figure(figsize=(10, 5))
    plt.plot(range(0, n + 1), rec_times, label='Рекурсивный метод')
    plt.plot(range(0, n + 1), iter_times, label='Итеративный метод')
    plt.xlabel('n')
    plt.ylabel('Время выполнения (с)')
    plt.title('Сравнение рекурсивного и итеративного методов')
    plt.legend()
    plt.grid(True)
    plt.show()

sravnenie(n)