import random
import time

def run():
    numero_random = random.randint(1,100)
    numero_elejido = int(input("Elige un numero del 1 al 100: "))
    while numero_elejido != numero_random:
        if numero_elejido < numero_random:
            time.sleep(1.5)
            print("Habrás ganado....?")
            time.sleep(1.5)
            print("No ganaste...")
            time.sleep(1.5)
            numero_elejido = int(input("Elige un numero mas grande: "))
        else:
            time.sleep(1.5)
            print("Habrás ganado....?")
            time.sleep(1.5)
            print("No ganaste...")
            time.sleep(1.5)
            numero_elejido = int(input("Elige un numero mas pequeño: "))
    time.sleep(1.5)
    print("Habrás ganado....?")
    time.sleep(1.5)
    print("Ganaste perro")


if __name__ == "__main__":
    run()
