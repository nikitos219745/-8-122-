import numpy as np
while True:

    a = 3
    b = 3
    masiv = []
    masiv2=[]
    for i in range(a):
        d=[]      #проміжний масив             
        for j in range(b):
            while True:
                try:        #перевірка на входжен інтового числа
                    d.append(int(input("введите первую матрицу по елементно:")))
                    break
                except ValueError:
                    print ("Vedi int plz")
        masiv.append(d)

        for i in range(a):
        c=[]                  #такі самі дії як і в 1 варіанті
        for j in range(b):
            while True:
                try:       #перевірка на помилки
                    c.append(int(input("введите вторую матрицу по елементно:"))) #додаєм введені числа в проміжний масив 
                    break
                except ValueError:
                    print ("vedi in plz")
        masiv2.append(c) #додаєм в початковий масив елементи з проміжного



    c=np.array(masiv)
    b=np.array(masiv2)
    print(c.dot(b))
    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
