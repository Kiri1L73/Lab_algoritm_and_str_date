import time
import sys

n = int(input("Введите число n: "))

start_time = time.time()

# Увеличиваем лимит глубины рекурсии
sys.setrecursionlimit(100000)

def sum_of_digits(num):
    return sum(int(d) for d in str(num))

def recursive(current, n):
    if current > n:
        return []

    str_current = str(current)

    if (len(str_current) > 2 and int(str_current[0]) <= 5 and sum_of_digits(current) >= 10):
        return [current] + recursive(current + 2, n)
    else:
        return recursive(current + 2, n)

def algoritm_sposob(n):
    return recursive(2, n)

numbers_algorithmic = algoritm_sposob(n)
end_time = time.time()

print(numbers_algorithmic)
print(f"Время выполнения: {end_time - start_time:.5f} секунд")


