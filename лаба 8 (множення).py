import numpy as np
print('Вибери розмірність матриці')
n = int(input("Введи к-ль стовпців 1 матриці"))
m = int(input("Введи к-ль рядків 1 матриці"))
b = int(input("Введи к-ль стовпців 2 матриці"))
v = int(input("Ввели к-ль рядків 2 матриці"))



A = np.zeros((n, m), dtype = int)           
B = np.zeros((b, v), dtype = int)            

while True:
    try:
        q = int(input ("Вибери розмірність кінцевої матриці:  "))
        break
    except ValueError:
        print("Введи шось інтове")

while True:
    try:
        g = int(input ("Вибери розмірність кінцевої матриці:  "))
        break
    except ValueError:
        print("Введи шось інтове")


i, j = 0, 0

for i in range(q):
    for j in range(g):
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
 
i, j = 0, 0
N=[[sum(map(lambda x: x[0]*x[1],zip(A[i],[c[j] for c in B]))) for j in range(len(B[0]))] for i in range(len(A))]
print("result matrix")
for r in N:
    print(r)
