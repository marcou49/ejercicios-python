#coding: utf-8

print ("Muy buenas, vamos a calcular a cuantos km y millas estás de tu casa, vamos allá")
nombre = input('Antes de nada, ¿Cómo te llamas? ')



while True:

    km = float(input('A cuantos km vives de aquí '))

    millas = km * 0.6 #convertimos km en millas

    print( nombre + ' vives a ' + str(km) + ' km o lo que es lo mismo, a ' + str(millas ) + ' millas de aquí')
    respuesta = input('¿Quieres hacer otro calculo? (S/N):  ')
    respuesta = respuesta.lower()

    if respuesta == "s":
        print ('OK, vamos allá')

    elif respuesta != 'n' and respuesta != 's': # el usuario no contesta ni si ni no, afinamos la pregunta

        print('¿Si o NO? Teclea S si quieres hacer otro calculo o N por si ya has terminado')
        respuesta = input('¿Quieres hacer otro calculo? (S/N):  ')

    else:
        print('Hasta luego Lucas') # 'hasta luego Lucas' is a spanish expression like "Ciao bambino" ;)
        break
