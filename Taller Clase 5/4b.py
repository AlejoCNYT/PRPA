from math import comb

print("b) ¿Cuál es la probabilidad de que se necesiten 10 intervenciones? ")

k = 4
p = 0.64
r = 10 - k # Número de fracasos (en este caso, 10 - 4 = 6, ya que necesitamos 10 operaciones en total y 4 son éxitos)

P = comb(r + k - 1, r) * (p ** k) * ((1-p) ** r)

res = round(P * 100, 2)

print(f"P (X = {r})", res)
