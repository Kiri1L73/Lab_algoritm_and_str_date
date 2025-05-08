import time
import sys

n = int(input("Введите число n: "))

start_time = time.time()

sys.setrecursionlimit(100000)

def recursive(current, n):
    if current > n:
        return []
    if int(str(current)[0]) <= 5:
        return [current] + recursive(current + 2, n)
    else:
        return recursive(current + 2, n)

def algoritm_sposob(n):
    return recursive(2, n)

numbers_algorithmic = algoritm_sposob(n)
end_time = time.time()

print(numbers_algorithmic)
print(f"Время выполнения: {end_time - start_time:.5f} секунд")
