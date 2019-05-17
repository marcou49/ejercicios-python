#coding: utf-8
secreto = 5
adivina=int(input('Intenta adivinar el número secreto -> '))
while (adivina!=secreto):
 print('no no')
 adivina=int(input('intentalo de nuevo -> '))
print('Bravo, diste en el clavo, efectivamente era ' + str(secreto), '. Presiona una tecla para salir')
input('')

