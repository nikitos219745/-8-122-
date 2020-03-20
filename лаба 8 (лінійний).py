import numpy as np
import random
import timeit
while True:
    b= input("Якщо хочеш вввести числа сам натисни '1',для рандомізації натисни 'Enter' ")
    a = np.zeros(10, dtype=int)
    while True:
        try:
            x = int(input('Введи шукане число:  ')) #перевірка на входження інтового числа
            break
        except ValueError:
            print("Vedi intovoe")
    n = len(a)

    if b == '':
        while True:
            try:
                d1 = int(input('Введи мінімальне значеня: ')) #перевірка на входження інтового числа
                break              
            except ValueError:
                print ("chtoto  intovoe")
        while True:
            try:
                d2 = int(input('Введи максимальне значення: '))#перевірка на входження інтового числа
                break              
            except ValueError:
                print ("chtoto intovoe")

        for i in range(10):
            a[i] = random.randint(d1, d2)#створення рандомної послідовності від мін до макс


    else:  #в іншому випадку
        for i in range(10):#створення послідовності із 10 чисел 
            while True:
                try:           
                    a[i] = int(input(f'Enter {i + 1} element: '))#перевірка на входження інтового числа
                    break
                except ValueError:
                    print("int vedi")

    print(a)

    i = 0
    count = 0
    while i < n and a[i] != x:#створеня умови
        i += 1#рахівник для знаходженя положення
        count += 2
    if i == n:
        print('Ну не палучалась найти ,попробуй ше разок')#
    else:
        print("Шуканий елемент ", x ,"знайдений  на ",{i + 1}, "позиції")

    print("Порівняння виконувались ",count,"разів")

    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)#
    print("Програма була виконана за ",t,"секунд")
    if input('Натисни "Enter"  для перезавантаження: ') == '':
        continue
    break
