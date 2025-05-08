#Лабораторная работа #1 (вариант 15)
#ИСТбд-11, Хасанов Кирилл
#Целые четные шестнадцатеричные числа, начинающиеся с нечетных цифр и содержащие более 5 цифр.
#Для каждого числа минимальную и максимальную цифру вывести прописью.

import os

slovar = {
    '0': "ноль", '1': "один", '2': "два", '3': "три", '4': "четыре",
    '5': "пять", '6': "шесть", '7': "семь", '8': "восемь", '9': "девять",
    'A': "десять", 'B': "одиннадцать", 'C': "двенадцать",
    'D': "тринадцать", 'E': "четырнадцать", 'F': "пятнадцать"
}


def process_16_numbers(filename):
    if not os.path.exists(filename):
        print("Файл не найден.")
        return

    with open(filename, "r", encoding="utf-8") as file:
        for strok in file:
            words = strok.split()
            for word in words:
                if is_proverka_16(word):
                    min_digit, max_digit = min(word), max(word)
                    print(f"Число: {word} --- минимальная цифра: {slovar[min_digit]}, максимальная цифра: {slovar[max_digit]}")


def is_proverka_16(word):
    word = word.upper()
    if len(word) <= 5:
        return False
    if not all(c in "0123456789ABCDEF" for c in word):
        return False
    if int(word, 16) % 2 != 0:
        return False
    if word[0] in "02468":
        return False
    return True

filename = os.path.join(os.path.expanduser("~"), "Desktop", "dictionary.txt")

process_16_numbers(filename)
