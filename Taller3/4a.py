from math import comb

print("a) ¿Cuál es el valor de intervenciones que se espera que deba padecer el paciente? ", end='')

k = 4
p = 0.63

E = k / p
res = round(E + 4, 1)

print("\n")
print(f"E(X={k}) =", res)


