import numpy as np
a=3
b=3
mas=[]     #створюємо масив
for i in range(a): 
    d=[]# створюємо  проміжний масив
    for j in range(b):
        d.append(int(input("введите первую матрицу по елементно:")))# додаєм введені елементи в проміж.масив   mas.append(d)
a = np.array(mas)
a = a.transpose()#транспонуємо
print(a)#виводим
