pregunta = str(input("Queres arrancar? "))
plata = 500

while pregunta == "si":
    apuesta = int(input("Cuanto desea aportar? "))

    if (apuesta >= 0) and (apuesta <= plata):
        from random import randint

        #saca carta random
        def sacar_carta() ->int:
            carta = randint(1,10)
            return carta

        #decalaramos jugador y le sumamos la carta sacada
        mazo = sacar_carta()
        jugador = 0
        crupier = 0
        jugador = jugador + mazo

        #se le informa al jugador cuanto tiene, y se le pregunta si quiere sacar otra carta
        print(f'Usted tiene: {jugador}')
        respuesta = input('Quiere pedir otra carta?  ')

        #Si tiene menos de 21 y quiere otra carta, loop sumandole lo que tiene, se le informa y se le vuelve a preguntar si quiere una nueva carta
        if respuesta == "si":
            while (jugador < 21) and (respuesta == "si"): # Repetición del juego
                mazo = sacar_carta()
                jugador = jugador + mazo
                print(f'Usted tiene: {jugador}')
                if jugador < 21:
                    respuesta = input('Quiere pedir otra carta?  ')
            if jugador > 21: 
                print("Te pasaste de 21")
            elif (respuesta == "no"):
                print(f"Te plantaste en {jugador}")
        else:
            print(f"Te plantaste en {jugador}")

        mazo = sacar_carta()
        crupier = jugador + mazo

        #se le informa al jugador cuanto tiene el crupier
        print(f'Crupier tiene: {crupier}')
        
        while ((crupier < 16) and (crupier < 21)) or (crupier < jugador): # Turno del crupier
            mazo = sacar_carta()
            crupier = jugador + mazo
            print(f'Crupier tiene: {crupier}')

        if (jugador < 21) and (crupier < 21):
            if jugador > crupier :
                plata = plata + apuesta
                print(f"Gano Jugador y ahora tu dinero es {plata}")
            else:
                plata = plata - apuesta
                print(f"Gano Crupier y ahora tu dinero es {plata}")
        elif jugador > 21:
                plata = plata - apuesta
                print(f"Gano Crupier y ahora tu dinero es {plata}")
        elif crupier > 21 : 
                plata = plata + apuesta
                print(f"Gano Jugador y ahora tu dinero es {plata}")
    else:
        print("Esa apuesta no es posible")

    pregunta = str(input("Queres volver a jugar? "))