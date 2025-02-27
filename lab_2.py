#Лабораторная работа #2 (вариант 15)
#ИСТбд-11, Хасанов Кирилл
#Целые четные шестнадцатеричные числа, начинающиеся с нечетных цифр и содержащие более 5 цифр.
#Для каждого числа минимальную и максимальную цифру вывести прописью.
#Изменения:
#1.	Входной файл является обыкновенным (т.е. нет требования на «бесконечность» файла);
#2.	Распознавание и обработку делать  через регулярные выражения;
#3.	В вариантах, где есть параметр (например К), допускается его заменить на любое число(константу);
#4.	Все остальные требования соответствуют варианту задания лабораторной работы №1.
import random
import os
import re

slovar = {
    '0': "ноль", '1': "один", '2': "два", '3': "три", '4': "четыре",
    '5': "пять", '6': "шесть", '7': "семь", '8': "восемь", '9': "девять",
    'A': "десять", 'B': "одиннадцать", 'C': "двенадцать",
    'D': "тринадцать", 'E': "четырнадцать", 'F': "пятнадцать"
}

# Регулярное выражение для проверки шестнадцатеричного числа
regular_16 = re.compile(r"^[13579BDF][0-9A-F]{5,}$")  # Первая цифра нечетная, кол-во цифр > 5

def generate_16_numbers(filename, count=500):
    with open(filename, "w", encoding="utf-8") as file:
        for _ in range(count):  # Генерация 500 чисел
            dlina_digit = random.randint(6, 10)  # Длина числа от 6 до 10
            number = "".join(random.choices("13579BDF" + "0123456789ABCDEF", k=9))
            if int(number, 16) % 2 == 0:
                file.write(number + " ")  # Запись числа в файл через пробел

def process_16_numbers(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            words = line.split()  # Разбиваем строку на числа по пробелу
            for word in words:
                if is_proverka_hex(word):
                    min_digit, max_digit = min(word), max(word)
                    print(f"Число: {word} --- минимальная цифра: {slovar[min_digit]}, максимальная цифра: {slovar[max_digit]}")

def is_proverka_hex(word):
    # Проверка, на соответствие слова регулярному выражению
    return regular_16.match(word) and int(word, 16) % 2 == 0

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "dictionary.txt")

generate_16_numbers(desktop_path)
process_16_numbers(desktop_path)
