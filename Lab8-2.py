import time
import numpy as np
import matplotlib.pyplot as plt

# Definir los valores de a y b
a = 10.0
b = 15.0

# Número de repeticiones para la suma en cada experimento
N = 10000

# Número de experimentos
k = 100000

# Lista para almacenar los tiempos promedio de cada experimento
tiempos_promedio = []

# Realizar el experimento k veces
for _ in range(k):
    inicio = time.time()

    # Realizar la operación de suma N veces
    for _ in range(N):
        resultado = a + b

    fin = time.time()

    # Calcular el tiempo promedio para este experimento y almacenarlo
    tiempo_promedio = (fin - inicio) / N
    tiempos_promedio.append(tiempo_promedio)

# Convertir la lista de tiempos promedio a un arreglo de numpy
tiempos_promedio = np.array(tiempos_promedio)

# Graficar la distribución de los tiempos promedio
plt.hist(tiempos_promedio, bins=50, color="blue", alpha=0.7)
plt.xlabel("Tiempo promedio (segundos)")
plt.ylabel("Frecuencia")
plt.title("Distribución de los tiempos promedio para la operación de suma")
plt.show()

# Imprimir resultados
print("Valores que se utilizaron para a y b:", a, b)
print("Resultados:")
print("Tiempo promedio total:", np.mean(tiempos_promedio))
print("Desviación estándar de los tiempos promedio:", np.std(tiempos_promedio))
