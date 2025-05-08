import tkinter as tk
from tkinter import scrolledtext
import itertools
import time


def sum_of_digits(num):
    return sum(int(d) for d in str(num))


def filter_even_numbers(n):
    even_numbers = itertools.count(start=2, step=2)
    limited = itertools.takewhile(lambda x: x <= n, even_numbers)

    result = list(filter(lambda x: int(str(x)[0]) <= 5 and len(str(x)) > 2, limited))
    return result


def calculate_filtered_numbers():
    try:
        n = int(entry_n.get())

        if n < 2:
            raise ValueError("n должно быть больше или равно 2.")

        start_time = time.time()
        result = filter_even_numbers(n)
        end_time = time.time()

        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Числа, выполняющие условие:\n")
        output_text.insert(tk.END, "\n".join(str(x) for x in result) + "\n\n")
        output_text.insert(tk.END, f"Найдено: {len(result)} чисел\n")
        output_text.insert(tk.END, f"Время выполнения: {end_time - start_time:.4f} секунд")

    except ValueError as e:
        messagebox.showerror("Ошибка ввода", str(e))

root = tk.Tk()
root.configure(bg='lightgreen')
root.geometry('500x500+400+100')
root.title("Вывод чётных чисел по условиям")

font = ('Arial', 14)

label_n = tk.Label(root, text="Введите число n:", font=font, bg='lightgreen', fg='saddlebrown')
label_n.pack(pady=5)

entry_n = tk.Entry(root, font=font, width=10, bg='white', fg='black')
entry_n.pack(pady=5)

button_calculate = tk.Button(root, text="Вывести", command=calculate_filtered_numbers, font=font, width=20)
button_calculate.pack(pady=10)

output_text = scrolledtext.ScrolledText(root, width=50, height=15, font=font)
output_text.pack(pady=10)

root.mainloop()