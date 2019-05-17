#coding:utf-8

lista = True
intentos = 0

while lista == True:

    numero = input("Pon un numero del 1 al 20\n ")
    numero = int(numero)

    if numero > 1 and numero < 21 : #comprobamos que el numero está entre 1 y 20

        lista = False

    else:

        if intentos < 1:
            print("Picha, te hemos dicho entre 1 y 20, centrate") #le avisamos que se está equivocando
            intentos += 1 #sumamos un intento

        else:
            print("Eres muy tonto anda vete")
            quit()



for i in range(1,numero+1):

    if i % 3 == 0 and i % 5 == 0:

        print('biz-zum')

    elif i % 3 == 0:

       print('biz')

    elif i % 5 == 0:

        print('zum')

    else:

        print(i)