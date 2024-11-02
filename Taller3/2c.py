from scipy.stats import poisson

print("c. ¿cuál es la probabilidad de que fallen por lo menos 11 en 125 horas?")

lambda_100 = 8

lambda_125 = (125 / 100) * lambda_100
prob_c = 1 - poisson.cdf(10, lambda_125)

print(f"c) La probabilidad de que fallen al menos 11 componentes en 125 horas es {prob_c:.4f}")

