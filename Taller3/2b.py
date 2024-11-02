from scipy.stats import poisson

lambda_100 = 8

print("b. ¿y de que fallen no más de dos componentes en 50 horas?")

lambda_50 = (50 / 100) * lambda_100
prob_b = poisson.cdf(2, lambda_50)

print(f"b) La probabilidad de que fallen no más de dos componentes en 50 horas es {prob_b:.4f}")
