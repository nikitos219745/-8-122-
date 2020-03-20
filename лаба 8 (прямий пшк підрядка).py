import random
import timeit

while True:
    text = "Сьогодні я вивчив новий метод по роботі з масивами"#наше початкове реченяя 
    f = input("Якщо хочеш вввести речення сам натисни '1',для автоматично вибору натисни 'Enter'")
    if f == '':
        string = ['я', 'метод ', 'по']#занесення в масив підрядків
        p = random.choice(string)
        print(f'Desired string is "{p}"')

    else:
        p = input('Введіть ваше речення: ') 
        print("Ваше речення це:     ",p)
    i = -1               #індекси рядка
    j = 0               #індекси підрядка
    count = 0
    while (j < len(p)) and i < (len(text) - len(p)):
        j = 0
        i += 1
        count += 2
        while j < len(p) and p[j] == text[i + j]:
             j += 1
             count += 2
    if j == len(p):
        print("Підрядок знайдений на ",i + 1, "позиції")
    else:
        print('Підрядок не знайдений ')




    timeit = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print("Пограма була виконана за ",timeit )

    if input('Нажмите "Enter"  для Перезавантаження ,а цифру або букву для завершення: ') == '':
        continue
    break
