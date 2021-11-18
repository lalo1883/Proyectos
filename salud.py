
subi_bajar = """ 

Hola! aquí te ayudaremos a revisar cuantos nutrientes serían ideales
que consuimieras según tu estilo de vida.

Primero que nada te vamos a preguntar tus metas y cuanto ejercicio haces...

 (1) Es para personas que quieren bajar o mantener su peso, (2) Personas que quieran subir de masa muscular.

1a - para personas sedentarias, bajar de peso.
1b - para personas con poca actividad física (ejercicio de 1 a 3 veces por semana) , bajar de peso.
1c - para individuos que realizan actividad moderada (ejercicio de 3 a 5 veces por semana) , bajar de peso.
1d -  para personas que hacen actividad intensa (ejercicio de 6 a 7 veces por semana) , bajar de peso.
1e - para atletas profesionales (entrenamientos de más de 4 horas diarias), bajar de peso.

2b - para personas sedentarias, subir de peso.
2c - para personas con poca actividad física (ejercicio de 1 a 3 veces por semana) , subir de peso.
2c - para individuos que realizan actividad moderada (ejercicio de 3 a 5 veces por semana) , subir de peso.
2d -  para personas que hacen actividad intensa (ejercicio de 6 a 7 veces por semana) , subir de peso.
2e - para atletas profesionales (entrenamientos de más de 4 horas diarias), subir de peso.

// SELECIONA LA TECLA QUE APARECE EN EL MENU //

"""
opcion = input(subi_bajar)


def ideal(deseoejer, deseopro):
    peso = input("Ingresa tu peso en KG: ")
    altura = input("Altura en CM: ")
    edad = input("Ingresa tu edad: ")

    peso = float(peso)
    altura = float(altura)
    edad = float(edad)

    proteinas = peso * deseopro
    creatina = peso / 9
    calorias = 66 + (13.7 * peso) + (5 * altura) - (6.8 * edad )
    calorias = calorias * deseoejer

    proteinas = str(proteinas)
    creatina = str(creatina)
    calorias = str(calorias)

    print("debes de consumir " + proteinas + " gramos de proteinas al día")
    print("debes de consumir " + creatina + " gramos de creatina al día")
    print("debes de consumir " + calorias + " calorias al día")

    
if opcion == "1a":
    ideal(1.2,.8)
elif opcion == "1b":
    ideal(1.375,.8)
elif opcion == "1c":
    ideal(1.55,.8)
elif opcion == "1d":
    ideal(1.725,.8)
elif opcion == "1e":
    ideal(1.9,.8)
elif opcion == "2a":
    ideal(1.2,1.2)
elif opcion == "2b":
    ideal(1.375,1.4)
elif opcion == "2c":
    ideal(1.55,1.5)
elif opcion == "2d":
    ideal(1.725,1.75)
elif opcion == "2e":
    ideal(1.9,2)
else:
    print("Elige una opción correcta!")


    


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