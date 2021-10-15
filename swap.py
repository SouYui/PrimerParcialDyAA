# ! Recibe un valor de tipo entero
# R Devuelve el resultado de la operación del factorial del número insertado
def factorial(valor):
    bandera = 1
    primera = 1
    segunda = 2
    while bandera < valor:
        primera = primera * segunda
        segunda = segunda + 1
        bandera = bandera + 1
    return(primera)

# ! Recibe tres parámetros de entrada: una lista de datos y dos índices a intercambiar su posición
# R Devuelve la lista con los elementos de los índices intercambiados entre sí
def swap(lista, indiceUno, indiceDos):
    auxi = lista[indiceUno]
    lista[indiceUno] = lista[indiceDos]
    lista[indiceDos] = auxi