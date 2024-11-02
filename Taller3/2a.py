print("a. ¿cuál es la probabilidad de que falle un componente en 25 horas?")

from scipy.stats import poisson

lambda_100 = 8

lambda_25 = (25 / 100) * lambda_100
prob_a = poisson.pmf(1, lambda_25)

# Mostramos los resultados
print(f"a) La probabilidad de que falle un componente en 25 horas es {prob_a:.4f}")


