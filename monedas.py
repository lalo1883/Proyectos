menu = """ Bienvenido al menú del conversor de monedas 💵

1- Pesos Mexicanos
2- Pesos Colombianos
3- Pesos Argentinos

Elige una opción:
"""
opcion = input(menu)


def conversor(valordolar, pais):
    pesos = input("Cuántos pesos " + pais + " tienes?: ")
    pesos = float(pesos)
    valor_dolar = (valordolar)
    dolares_tuyos = pesos / valor_dolar
    dolares_tuyos = round(dolares_tuyos, 2)
    dolares_tuyos = str(dolares_tuyos)
    print("Tienes " + dolares_tuyos + " dolares")


if opcion == "1":
    conversor(20, " mexicanos")
elif opcion == "2": 
    conversor(3771.86, " colombianos")
elif opcion == "3":
    conversor(99.15, " argentinos")
else:
    print("Ingresa una opción correcta!")
 