n=1
while n<=2:
    f=input('сколько будит числ :')
    if f.isalpha():
        print('попробуй ище раз  ')
    else:
        spisok = []
        f= int(f)
        for i in range (f): #формируем список , спросить за i
            x=input("введите число. \n")
            if x.isdigit():
                spisok.insert(i,x) #питаемся сложить
            else:
                print('ну значит на одно меньше будит ')
        print(spisok)
        print(max(spisok))
        n+=2