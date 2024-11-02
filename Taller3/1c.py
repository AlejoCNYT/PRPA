from math import comb

print("Probabilidad de que por lo menos una se encuentre defectuosa")

n = int(input("n= "))
p = float(input("p= "))
q = 1 - p

C = comb(n, 0)
P = ( (C * (p**0) * (q**n) ) * 100)
print(P)

print(f"P(X >= 1) = ", round(P, 3), "%")
