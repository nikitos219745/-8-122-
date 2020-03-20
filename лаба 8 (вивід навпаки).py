import numpy as np
mas = []
for i in range(3):
    d=[]    #створюємо проміжний масив куда будемо зберігати введені елементи
    for j in range(3):
        d.append(int(input("Введіть першу матрицу по елементно:")))
    mas.append(d) #додаєм введені елементи в початковий масив
for k in range(len(mas)):
    s=np.array(mas)
    x=s[::-1] # створюємо цикл та робим зріз так щоб елементи виводились навпаки
print(x)
