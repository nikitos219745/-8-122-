import numpy as np
while True:
    while True:
        while True:
            try:
                while True:
                    try:
                        n = int(input('Кількість рядків 1 матриці: '))
                        m = int(input('Кількість стовчиків 2 матриці: '))
                        break
                    except ValueError:
                        print ("Vedi chislo")


                while True:
                    try:
                        k = int(input('Кількість рядків 2 матриці: '))
                        l = int(input('Кількість стовпчиків 2 матриці: '))
                        break
                    except ValueError:
                        print("ne mychay komp ,vedi chislo")
                       

                A, B = np.zeros((n, m), dtype=int), np.zeros((k, l), dtype=int)  # Ініціалізація двох матриць нулями.
                for i in range(n):
                    for j in range(m):                      
                        if n == 3 and m == 3 and k == 3 and l == 3:    #перевірка умови на розмірність
                            while True:
                                try:
                                    A[i, j] = int(input(F' A([{i + 1}, {j + 1}]): '))
                                    break
                                except ValueError:
                                    print("vedi chislo")
                            while True:
                                try:     
                                    B[i, j] = int(input(F' B([{i + 1}, {j + 1}]): '))
                                    break
                                except ValueError:
                                    print ("chislo vedi")


                        elif n != 3 or m != 3 and k != 3 or l != 3:
                            print('Розмірність НЕ 3 на 3 ')
                        elif n > 3 or m > 3 and k > 3 or l > 3:
                            print('Розмірність НЕ 3 на 3')
                break
            except ValueError:  # Перевірка на ввод 
                print('Введіть числа! ')
        N = np.zeros((k, l), dtype=int)                            #кінцева матриця 
        F = 0                                                      # зміна яка відповідає множення стовпчика на рядок
        T = np.zeros((k, l), dtype=int)                            #створення проміжного масиву
        
        for i in range(n):                                         #  створюємо два цикли для того щоб отримати доступ до елементів рядка першої матриці та стопчика другої матриці
            for j in range(l):                   
                T[i, j] = B[j, i]
                F = A[i - 2] * T[i - 2]                            # створення змінної де будем зберігати значеня добутку рядка на рядок
                
                                                                        
                N[0, 0] = F[i - 2] + F[i - 1] + F[i]
                F = A[i - 2] * T[i - 1]
                N[0, 1] = F[i - 2] + F[i - 1] + F[i]
                F = A[i - 2] * T[i]                              #Обробка пешого рядка матриці Н
                N[0, 2] = F[i - 2] + F[i - 1] + F[i]
                F = A[i - 1] * T[i - 2]
                            
                N[1, 0] = F[i - 2] + F[i - 1] + F[i]
                F = A[i - 1] * T[i - 1]
                N[1, 1] = F[i - 2] + F[i - 1] + F[i]             #Обробка другого рядка матриці Н
                F = A[i - 1] * T[i]
                N[1, 2] = F[i - 2] + F[i - 1] + F[i]
                F = A[i] * T[i - 2]
                
                N[2, 0] = F[i - 2] + F[i - 1] + F[i]
                F = A[i] * T[i - 1]                               #Обробка третього рядка матриці Н
                N[2, 1] = F[i - 2] + F[i - 1] + F[i]             
                F = A[i] * T[i]
                N[2, 2] = F[i - 2] + F[i - 1] + F[i]
                print('Результат добутку: ', N)
    if input('Натисни "Enter"  для перезавантаження: ') == '':
            continue
    break

         
