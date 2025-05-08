import timeit
import math

n = int(input("Введите число n: "))

def recursive(n, memo={0: 1, 1: 1}):
    if n in memo:
        return memo[n]
    else:
        result = (-1) ** n * (2 * recursive(n - 1, memo) / math.factorial(n) + recursive(n - 2, memo))
        memo[n] = result
        return result

def iterative(n):
    if n == 0 or n == 1:
        return 1
    znach_1 = 1  # F(0)
    znach_2 = 1  # F(1)
    for i in range(2, n + 1):
        last = (-1) ** i * (2 * znach_2 / math.factorial(i) + znach_1)
        znach_1 = znach_2
        znach_2 = last
    return last

def time_it(func, n):
    return timeit.timeit(lambda: func(n), number=1)

def sravnenie(n):
    print(f"{'n':>3} | {'Rec (s)':>10} | {'Iter (s)':>10} | {'F_rec(n)':>14} | {'F_iter(n)':>10}")
    print('-' * 62)
    for i in range(0, n + 1):
        # Рекурсивное вычисление
        try:
            rec_result = recursive(i)
            rec_time = time_it(recursive, i)
        except RecursionError:
            rec_result = 'RecursionError'

        # Итеративное вычисление
        iter_result = iterative(i)
        iter_time = time_it(iterative, i)

        znachenie_rec = f"{rec_result:.10f}" if isinstance(rec_result, (float, int)) else str(rec_result)
        znachenie_iter = f"{iter_result:.10f}" if isinstance(iter_result, (float, int)) else str(iter_result)

        print(f"{i:>3} | {rec_time:>10.6f} | {iter_time:>10.6f} | {znachenie_rec:>14} | {znachenie_iter:>10}")

sravnenie(n)