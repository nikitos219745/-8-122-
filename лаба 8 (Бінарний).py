import numpy as np
import random
import timeit

while True:
    
    f = input("Якщо хочеш вввести числа сам натисни '1',для рандомізації натисни 'Enter' ")
    a = np.zeros(10, dtype=int)#задаєм к-ль чисел що будуть генеруватись
    while True:
        try:
            x = int(input("Введи шукане число: "))#перевірка на входженн яінтового числа
            break
        except ValueError:
            print("vedi int")


    n = len(a)
    if f == '':
        while True:
            try:
                d1 = int(input('Введи мінімальне число з якого буде починатись послідовність: '))#задаєм діапазон мінімального знач
                break
            except ValueError:
                print ("Vedi int")

        while True:
            try:
                d2 = int(input('Введи максимальне число яким буде закінчуватись послідовність:  '))#задаєм діапазон максимального знач
                break
            except ValueError:
                print ("Vedi int")



        for i in range(10):
            a[i] = random.randint(d1, d2)

    else:
        for i in range(10):#створення послідовності
            while True:
                try:
                    a[i] = int(input(f'Enter {i + 1} element: '))#перевірка на інт число
                    break
                except ValueError :
                    print( "vedi int")
    print(a)

    a = sorted(a)
    print(a)
    l = 0
    r = len(a) - 1
    k = 0
    count = 0
    f = False

    while l <= r and not f:    #
        count += 2             #
        k = (l + r) // 2       #
        if a[k] == x:          #
            f = True           #
        elif a[k] < x:         # УМОВА ВІДПОВІДНОСТІ  ЕЛЕМЕНТА 
            count += 1         #
            l = k + 1          #  
        else:                  #
            count += 1         #
            r = k - 1          #
    if not f:
        print('Ну не палучалась найти ,попробуй ше разок')
    else:
        print("Шуканий елемент ", x ,"знайдений  на ",{k + 1}, "позиції")
    print("Порівняння виконувались ",count,"разів")

    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print("Програма була виконана за ",t,"секунд")

    if input('Нажмите "Enter"  для перезавантаження: ') == '':
        continue
    break
