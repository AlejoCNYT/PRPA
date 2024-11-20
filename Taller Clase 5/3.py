from itertools import product
from traceback import print_exc

print("Calculando la probabilidad de necesitar más de tres lanzamientos")

numero_lanzamientos_max = int(input("Ingrese el numero maximo de lanzamientos: "))
n = numero_lanzamientos_max - 1
numero_lanzamientos = 0
Probabilidades_lista = []

while numero_lanzamientos < numero_lanzamientos_max:
    probabilidad = []  # 1 / 6 = 0.16666666666
    # Crear una sublista para cada lanzamiento y agregar las probabilidades
    for index in range(n - numero_lanzamientos + 1):
        if index == 0:
            probabilidad.insert(index,0.16666666666)
        else:
            m = 0.16666666666*5
            probabilidad.insert(index, m)
    Probabilidades_lista.append(probabilidad)
    numero_lanzamientos += 1

producto_lista = []

for y in range(len(Probabilidades_lista)):
    producto = 1
    for x in range(len(Probabilidades_lista[y])):
        producto *= Probabilidades_lista[y][x]
    producto_lista.append(producto)

Pn = (1 - producto_lista[0]) * 100

print(f"P({index+1}) = ", Pn, "%")
