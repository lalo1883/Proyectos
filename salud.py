
subi_bajar = """ Hola! aquí te ayudaremos a revisar cuantos nutrientes serían ideales
que consuimieras según tu estilo de vida.

Primero que nada, selecciona cuanto ejercicio haces.

a - para personas sedentarias
b - para personas con poca actividad física (ejercicio de 1 a 3 veces por semana).
c - para individuos que realizan actividad moderada (ejercicio de 3 a 5 veces por semana).
d -  para personas que hacen actividad intensa (ejercicio de 6 a 7 veces por semana).
e - para atletas profesionales (entrenamientos de más de 4 horas diarias).

// SELECIONA LA TECLA QUE APARECE EN EL MENU //

"""
opcion = input(subi_bajar)

def ideal(deseo):
    peso = input("Ingresa tu peso en KG: ")
    altura = input("Altura en CM: ")
    edad = input("Ingresa tu edad: ")

    peso = float(peso)
    altura = float(altura)
    edad = float(edad)

    proteinas = peso * 1.65
    creatina = peso / 9
    calorias = 66 + 13.7 * peso + 5 * altura + 6.8 * edad * deseo

    proteinas = str(proteinas)
    creatina = str(creatina)
    calorias = str(calorias)

    print("debes de consumir " + proteinas + " gramos de proteinas al día")
    print("debes de consumir " + creatina + " gramos de creatina al día")
    print("debes de consumir " + calorias + " calorias al día")

    
if opcion == "a":
    ideal(1.2)
elif opcion == "b":
    ideal(1.375)
elif opcion == "c":
    ideal(1.55)
elif opcion == "d":
    ideal(1.725)
elif opcion == "e":
    ideal(1.9)


    


# def run():
#     peso = input("Ingresa tu peso en KG: ")
#     altura = input("Altura en CM: ")
#     edad = input("Ingresa tu edad: ")

#     peso = float(peso)
#     altura = float(altura)
#     edad = float(edad)

#     proteinas = peso * 1.65
#     creatina = peso % 9
#     calorias = 66 + 13.7 * peso + 5 * altura + 6.8 * edad * 1.55

#     proteinas = str(proteinas)
#     creatina = str(creatina)
#     calorias = str(calorias)

    

#     print("debes de consumir " + proteinas + " gramos de proteinas al día")
#     print("debes de consumir " + creatina + " gramos de creatina al día")
#     print("debes de consumir " + calorias + " calorias al día")



# if __name__ == "__main__":
#     run()