############################# NO TOCAR ESTE CÓDIGO ############################
from random import randint

def sacar_carta() ->int:
    carta = randint(1,10)
    return carta


######################## EJEMPLO DE USO DE SACAR_CARTA ########################
#c = sacar_carta()
#print(c)
#En la consola se vería:    8

########################### AQUÍ COMIENZA TU CÓDGIO ###########################
mazo = sacar_carta
jugador = 0
crupier = 0
jugador = jugador + mazo
while jugador < 21: # Repetición del juego
    print(f'usted tiene{jugador}')
    respuesta = input('quiere pedir otra carta(si o no)?  ')
    while respuesta == "si": # Turno del jugador
        jugador = jugador + mazo
        print(f'usted tiene{jugador}')



        jugador = jugador + mazo
    while(): # Turno del crupier
        print("hola")
