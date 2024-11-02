import math
from math import factorial

print("c. ¿cuál es la probabilidad de que fallen por lo menos 11 en 125 horas?")

lambda_ = 10
k = 0
e = math.e

suma_res = 0

while k < lambda_ :
    P = ((e**(-lambda_)) * (lambda_**k)) / factorial(k)
    k += 1
    suma_res += P

res = 1 - suma_res

print(f"P(X >= {k}) =", round(res * 100, 3), "%")
