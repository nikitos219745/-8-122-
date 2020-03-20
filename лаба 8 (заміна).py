import numpy as np
while True:

        try:
            n = int(input('Введіть кількість рядків: '))                 
        except ValueError:
            print('шось інтове')
            break
    
        try:
             m = int(input('Введіть кількість стовпців: '))              
        except ValueError:
            print('шото інтове ')
            break


        A = np.zeros((n, m), dtype=int)  # створюємо матрицю з нулями
        for i in range(n):  
            for j in range(m):
                if n == 4 and m == 4:  #Перевіряємо  на розмірність
                    while True:
                        try:
                            A[i, j] = int(input(f' [{i + 1}, {j + 1}]: '))
                            break
                        except ValueError:
                            print("Число ,а не букву")
                    print(A)
                    if A[i, j] < 0: #умова при ,якій числа менше нуля будуть замінюватись на 0
                        A[i, j] = 0
        print(A)  
        if n != 4 or m != 4: #Перевірка на введення іншої матриці,не 4 на 4
            print('Введіть матрицю 4х4!')
        
        if input('Нажмите "Enter" для перезавантаження: ') == '':
            continue
        break
