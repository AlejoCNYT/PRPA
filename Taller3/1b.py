from math import comb

print("Probabilidad de que a lo sumo dos se encuentren defectuosas")

n = int(input("n= "))
k = int(input("k= "))
p = float(input("p= "))
q = p - 1

X = 0
while X <= k:
    if X == 0:
        print(f"P(X={X}) ", end='')
    else:
        print(end= '+ ')
        print(f"P(X={X}) ", end='')
    X += 1

X = 0
P_total = []

while X <= k:
    if X == 0:
        C = comb(n, X)
        P = C * (p**X) * ((1 - p)**(n - X))
        print('=', round(P, 3), end=' + ')
        P_total.append(P)
    else:
        C = comb(n, X)
        P = C * (p**X) * ((1 - p)**(n - X))
        print(round(P, 3), end=' + ')
        P_total.append(P)
    X += 1

suma = 0
for num in P_total:
    suma += num

res = round((suma * 100), 2)

print("=", res, "%")
