import time
import itertools

n = int(input("Введите число n: "))

start_time = time.time()

def sum_of_digits(num):
    return sum(int(d) for d in str(num))

# Начинаем с 2 с шагом 2
even_numbers = itertools.count(start = 2, step = 2)

limited = itertools.takewhile(lambda x: x <= n, even_numbers)

# Длина > 2, первая цифра ≤ 5, сумма цифр ≥ 10
result = list(filter(lambda x: int(str(x)[0]) <= 5 and sum_of_digits(x) >= 10 and len(str(x)) > 2, limited))

end_time = time.time()

print(result)
print(f"Время выполнения: {end_time - start_time:.5f} секунд")
