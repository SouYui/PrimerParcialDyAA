# Solución para el problema N° 3 de Diseño y Análisis de Algoritmos
# Autor: SouYui

def distancia_puntos(puntoInicial, puntoFinal):
    xInicial, yInicial = puntoInicial
    xFinal, yFinal = puntoFinal
    
    right = 0
    up = 0
    
    if(xFinal > xInicial):
        if(yFinal > yInicial):
            right = xFinal - xInicial
            up = yFinal - yInicial
        else:
            print("La posición no es válida, verifique su entrada")
    else:
        print("La posición no es válida, verifique su entrada")
    
    return (right, up)
        
def lista_elementos(distanciaX, distanciaY):
    listaResult = []
    
    if(type(distanciaX) == int and type(distanciaY) == int):
        for i in range(distanciaX):
            # 1 es igual a un movimiento a la derecha
            listaResult.append(1)
        for i in range(distanciaY):
            # 2 es igual a un movimiento a la izquierda
            listaResult.append(2)
    return listaResult

puntoUno = (5, 3)
puntoDos = (6, 8)

x, y = distancia_puntos(puntoUno, puntoDos)
lista = lista_elementos(x, y)
print(x, y)
print(lista)
