import numpy as np
while True:
    while True:
        try:
            while True:
                try:
                    n = int(input('Введіть кількість рядків: '))
                    break
                except ValueError:
                    print ("vedi int")
            while True:
                try:
                    m =  int(input('Введіть кількість стовпчиків: '))
                    break
                except ValueError:
                    print ("vedi int")

            V = np.zeros((n, m), dtype=int)   #створєм матрицю з нулями
            if n == 3 and m == 3:  #перевірка матриці
                for i in range(n):  
                    for j in range(m):
                        while True:
                            try:
                                V[i, j] = int(input(f' [{i+1}, {j+1}]: '))
                                break
                            except ValueError:
                                print("vedi int")
                print('Tвоя матриця: ',V)
            break
        except ValueError:  
            print('Vedi chislo ') #перевірка на число

    Trans = np.zeros((n, m), dtype=int)  #створення 2 матриці
    for i in range(m):  
        for j in range(n):
            Trans[i, j] = V[j, i]  #робим перезаміну зміних
    print( Trans)

    if input('Натисни "Enter"  для перезавантаження: ') == '':
        continue
    break
