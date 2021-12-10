contadorJ1 = 0 
contadorJ2 = 0

def obtenerPuntosJ1(linea):
    partes = linea.split(",")
    if partes[0].lower() == "jugador 1":
        suma = int(partes[1])+int(partes[2])
        return int(suma)
    else:
        return 0

def obtenerPuntosJ2(linea):
    partes = linea.split(",")
    if partes[0].lower() == "jugador 2":
        suma = int(partes[1])+int(partes[2])
        return int(suma)
    else:
        return 0

def calcularPuntajeJ1(puntos):
    puntajeJ1 = 0 
    if puntos == 7 or puntos == 11:
        puntajeJ1 = 3 
        return puntajeJ1
    elif puntos == 2 or puntos == 3 or puntos == 12:
        puntajeJ1 = -2
        return puntajeJ1
    elif puntos == 4 or puntos == 5 or puntos == 6 or puntos == 8 or puntos == 9 or puntos ==10:
        puntajeJ1 = 1
        return puntajeJ1
    else:
        return 0 

def calcularPuntajeJ2(puntos):
    puntajeJ2 = 0 
    if puntos == 7 or puntos == 11:
        puntajeJ2 = 3 
        return puntajeJ2
    elif puntos == 2 or puntos == 3 or puntos == 12:
        puntajeJ2 = -2
        return puntajeJ2
    elif puntos == 4 or puntos == 5 or puntos == 6 or puntos == 8 or puntos == 9 or puntos ==10:
        puntajeJ2 = 1
        return puntajeJ2
    else:
        return 0 


arch = open("./dados.txt","r",encoding=("UTF-8"))

linea = arch.readline().strip()

while linea != "":

    puntosObtenidosJ1 = obtenerPuntosJ1(linea)
    puntosObtenidosJ2 = obtenerPuntosJ2(linea)
    puntajeCalculadoJ1 = calcularPuntajeJ1(puntosObtenidosJ1)
    puntajeCalculadoJ2 = calcularPuntajeJ2(puntosObtenidosJ2)


    contadorJ1 += int(puntajeCalculadoJ1)
    contadorJ2 += int(puntajeCalculadoJ2)

    linea = arch.readline().strip()

print(">Puntaje Final del Jugador 1:",contadorJ1)
print(">Puntaje Final del Jugador 2:",contadorJ2)

def obtenerGanador(finalj1,finalj2):

    if finalj1 > finalj2:
        return str("1")
    elif finalj2>finalj1:
        return str("2")
    else:
        return str("ERROR")

print(">El ganador es Jugador",str(obtenerGanador(contadorJ1,contadorJ2)))
