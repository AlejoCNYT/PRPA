from math import comb

print("Probabilidad de que entre diez unidades, dos se encuentren defectuosas")

n = int(input("n= "))
k = int(input("k= "))
p = float(input("p= "))
q = p - 1

C = comb(n, k)
P = C * (p**k) * ((1 - p)**(n - k))

print(f"P(X = {k}) = ", round(P * 100, 2), "%")
