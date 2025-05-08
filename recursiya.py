# def generate_relay_orders(n):
#     def generate(arr, n):
#         if len(arr) == n:
#             result.append(tuple(arr))
#             return
#
#         for i in range(1, n + 1):
#             if i not in arr:
#                 arr.append(i)
#                 generate(arr, n)
#                 arr.pop()
#
#     result = []
#     generate([], n)
#     return result
#
# n = int(input("Введите количество спортсменов (n): "))
# orders = generate_relay_orders(n)
#
# for order in orders:
#     print(order)

# from itertools import permutations
#
# def generate_relay_orders(n):
#     athletes = list(range(1, n + 1))  # Создаем список спортсменов
#     all_orders = list(permutations(athletes))  # Генерируем все перестановки
#
#     return all_orders
#
#
# n = int(input("Введите количество спортсменов (n): "))
# orders = generate_relay_orders(n)
#
# for order in orders:
#     print(order)

def print_lower_triangle(matrix):
    size = len(matrix)
    result = []

    for i in range(size):
        for j in range(i + 1):
            result.append(matrix[i][j])

    print("Элементы нижней треугольной матрицы:")
    print(result)

n = int(input("Введите размер матрицы и её элементы: "))
matrix = [list(map(int, input().split())) for _ in range(n)]

print_lower_triangle(matrix)