import math
from math import factorial

print("a. ¿cuál es la probabilidad de que falle un componente en 25 horas?")

lambda_ = 8 / 2
k = 0
e = math.e
X = 2
suma_res = 0

while k <= X :
    P = ((e**(-lambda_)) * (lambda_**k)) / factorial(k)
    k += 1
    suma_res += P

res = round(suma_res * 100, 2)

print(f"P(X = {k-1}) =", res, "%")
