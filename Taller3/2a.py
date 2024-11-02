import math
from math import factorial

print("a. ¿cuál es la probabilidad de que falle un componente en 25 horas?")

lambda_ = 8 / 4
k = 1
e = math.e

P = ((e**(-lambda_)) * (lambda_**k)) / factorial(k)

res = round(P * 100, 2)

print(f"P(X = {k}) =", res)
