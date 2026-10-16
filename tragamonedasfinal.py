'''
Sofía Espinosa               Gustavo Espinoza
sofia.espinosa@alu.ucm.cl    gustavo.espinoza.01@alu.ucm.cl
Sección 3
25/10/2022
'''
from random import randint
import os
from time import sleep

#Limpia la pantalla
def limpiar():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

#Calcula la probabilidad de cada número
def tirada():
    ruleta = randint(1,100)
    if 1 <= ruleta <= 30:
        numero = 0
    elif 31 <= ruleta <= 50:
        numero = 1
    elif 51 <= ruleta <= 70:
        numero = 2
    elif 71 <= ruleta <= 80:
        numero = 3
    elif 81 <= ruleta <= 90:
        numero = 4
    elif 91 <= ruleta <= 95:
        numero = 5
    elif 96 <= ruleta <= 98:
        numero = 6
    else:
        numero = 7
    return numero

#Verifica si el valor es un Int
def verifica(valor):
    while valor.isdigit() == False:
        print("Formato incorrecto")
        sleep(1)
        valor = input("Reingrese su valor: ")
    return valor


#Monto inicial
#Dinero disponible para apuestas
def montoIn(monto):
    monto = int(monto)
    if int(monto) < 100:
        print("No tiene dinero suficiente para apostar")
        sleep(1)
        monto = input("Ingrese su monto inicial: ")
        monto = verifica(monto)
        montoIn(int(monto))
    else:
        apostado(monto)

#Monto apostado
def apostado(monto):
    apuesta = input("¿Cuánto dinero quiere apostar? \n $100    $500    $1000 \n -> $")
    apuesta= verifica(apuesta)
    apuesta = int(apuesta)
    if int(monto) < apuesta:
        print("No tienes dinero suficiente para realizar la apuesta.")
        sleep(1)
        apostado(monto)
    else:
        if apuesta == 100 or apuesta == 500 or apuesta == 1000:          
            resultado = [tirada(), tirada(), tirada()]
            print(resultado)
            ganaopierde(resultado, apuesta, monto)
            sleep(1)
        else:
            print("Apuesta inválida")
            sleep(1)
            apostado(monto)

#Tiradas ganadas o perdidas
#Se aplica el multiplicador de dinero según el resultado del tragamonedas
#res = resultado del tragamonedas
#apu = apuesta hecha
#mon = monto actual de dinero
def ganaopierde(res, apu, mon):
    ganancia = 0
    if res == [7,7,7]:
        ganancia = apu*1000
    elif res == [6,6,6]:
        ganancia = apu*250
    elif res == [5,5,5]:
        ganancia = apu*150
    elif res == [4,4,4] or res == [3,3,3]:
        ganancia = apu*50
    elif res == [2,2,2] or res == [1,1,1]:
        ganancia = apu*30
    elif res == [0,0,0]:
        ganancia = apu*20
    elif res.count(5) == 2 or res.count(6) == 2 or res.count(7) == 2:
        ganancia = apu*10
    elif res.count(7) == 1:
        ganancia = apu*5
    elif res.count(5) == 1 or res.count(6) == 1:
        ganancia = apu*2
    #Verifica si pierde o gana dinero
    else:
        print("Ha perdido $"+str(apu))
        mon = mon-apu
        print("Saldo actual: $"+str(mon))
    if ganancia != 0:
        print("Ha ganado $"+str(ganancia))
        mon = mon + ganancia
        print("Saldo actual: $"+str(mon))
    sleep(1)
    seguirjugando(mon)

#Pregunta si quiere seguir jugando
def seguirjugando(mon):
    if mon > 99:
        respuesta = input("¿Desea seguir jugando? \n Sí: 1  No: 2 \n -> ")
        respuesta = int(verifica(respuesta))
        if respuesta == 1:
            apostado(mon)
        elif respuesta == 2:
            limpiar()
            print("Juego terminado.")
            print("Saldo final: $"+str(mon))
            exit()
        else:
            print("Respuesta inválida")
            sleep(1)
            seguirjugando(mon)
    else:
        sleep(1)
        limpiar()
        print("No tiene dinero suficiente para seguir jugando.")
        print("Saldo final: $"+str(mon))
        exit()


if __name__ == "__main__":
    limpiar()
    monto = input("Ingrese su monto inicial: ")
    monto = verifica(monto)
    montoIn(monto)