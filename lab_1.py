#Лабораторная работа #1 (вариант 15)
#ИСТбд-11, Хасанов Кирилл
#Целые четные шестнадцатеричные числа, начинающиеся с нечетных цифр и содержащие более 5 цифр.
#Для каждого числа минимальную и максимальную цифру вывести прописью.
import random
import os
import time

slovar = {
    '0': "ноль", '1': "один", '2': "два", '3': "три", '4': "четыре",
    '5': "пять", '6': "шесть", '7': "семь", '8': "восемь", '9': "девять",
    'A': "десять", 'B': "одиннадцать", 'C': "двенадцать",
    'D': "тринадцать", 'E': "четырнадцать", 'F': "пятнадцать"
}

def generate_16_numbers(filename):
    with open(filename, "w", encoding="utf-8") as file:
        try:
            while True:  # Бесконечный цикл
                dlina_digit = random.randint(6, 10)
                number = "".join(random.choices("13579BDF" + "0123456789ABCDEF", k=dlina_digit))
                if int(number, 16) % 2 == 0:
                    file.write(str(number) + "  ") # Запись числа в файл через пробел
                    # file.write(number + "\n")  # Запись числа в файл с новой строки
                    time.sleep(0.01)
        except KeyboardInterrupt:  # Прерывание при остановке
            print("\nЗапись чисел была прервана пользователем")
            return

def process_16_numbers(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for strok in file:
            words = strok.split()
            for word in words:
                if is_proverka_hex(word):
                    min_digit, max_digit = min(word), max(word)
                    print(f"Число: {word} --- минимальная цифра: {slovar[min_digit]}, максимальная цифра: {slovar[max_digit]}")

def is_proverka_hex(word):
    if len(word) <= 5:
        return False
    if not all(c in "0123456789ABCDEF" for c in word.upper()):
        return False
    if int(word, 16) % 2 != 0:
        return False
    if word[0] in "02468":
        return False
    return True

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "dictionary.txt")

generate_16_numbers(desktop_path)

process_16_numbers(desktop_path)