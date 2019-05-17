# coding=UTF-8
mood = input("Cómo te encuentras hoy ¿Bien, regular o como un lunes? ")

if mood == "bien" or mood == "Bien":
    print("¡Olé! que suerte")
elif mood == "regular" or mood == "Regular":
    print("Animo")
elif mood == "como un lunes" or mood == "Como un lunes":
    print("Vamos que ya queda menos pal martes")
else:
print("No te entiendo picha")