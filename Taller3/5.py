from math import comb

print("5) Supongamos la extracción aleatoria de 8 elementos de un conjunto formado por 40 elementos totales, de los cuales 10 son del tipo A y 30 son del tipo B. Cuál es la probabilidad de obtener 4 objetos del tipo A? ")
print("\n")

N = int(input("Tamaño total de la población: "))
K = int(input("número total de elementos tipo A: "))
n = int(input("tamaño de la muestra: "))
k = int(input("número de elementos tipo A que queremos obtener: "))

P = ((comb(K, k) * comb(N-K, n-k)) / comb(N, n))

res = round(P * 100, 2)

print("\n")
print(f"P(X = {k}) =", res, "%")
