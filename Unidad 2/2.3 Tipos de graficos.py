# Parte 1: Importación de Librerías

# Empezaremos importando las librerías necesarias.
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Parte 2: Gráfico de Líneas

# El gráfico de líneas es ideal para mostrar tendencias a lo largo del tiempo.
# Vamos a crear un gráfico de líneas simple utilizando datos generados aleatoriamente.
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Gráfico de Líneas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()

# Parte 3: Gráfico de Barras

# Los gráficos de barras son útiles para comparar categorías.
# Crearemos un gráfico de barras para mostrar las ventas mensuales de un producto.
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
ventas = [10000, 12000, 11000, 9000, 9500]

plt.bar(meses, ventas)
plt.title('Ventas Mensuales')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.show()

# Parte 4: Gráfico de Pastel

# Los gráficos de pastel muestran las proporciones de diferentes categorías.
# Crearemos un gráfico de pastel para mostrar la distribución de ingresos por fuente.
fuentes = ['Publicidad', 'Ventas Directas', 'Alianzas', 'Patrocinios']
ingresos = [50000, 30000, 20000, 10000]

plt.pie(ingresos, labels=fuentes, autopct='%1.1f%%')
plt.title('Distribución de Ingresos')
plt.show()

# Parte 5: Gráfico de Dispersión

# Los gráficos de dispersión son útiles para visualizar la relación entre dos variables.
# Crearemos un gráfico de dispersión para mostrar la relación entre el precio y la demanda de un producto.
precio = np.random.randint(50, 200, 50)
demanda = np.random.randint(100, 1000, 50)

plt.scatter(precio, demanda)
plt.title('Relación Precio-Demanda')
plt.xlabel('Precio')
plt.ylabel('Demanda')
plt.show()

# Parte 6: Histograma

# Los histogramas son útiles para mostrar la distribución de una variable numérica.
# Crearemos un histograma para mostrar la distribución de edades en una muestra de población.
edades = np.random.randint(18, 80, 100)

plt.hist(edades, bins=10)
plt.title('Histograma de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

# Parte 7: Boxplot

# Los boxplots muestran la distribución de una variable numérica y posibles valores atípicos.
# Crearemos un boxplot para mostrar la distribución de salarios por nivel educativo.
salarios = {
    'Bachiller': np.random.normal(30000, 5000, 100),
    'Licenciatura': np.random.normal(40000, 7000, 100),
    'Maestría': np.random.normal(50000, 10000, 100)
}
df_salarios = pd.DataFrame(salarios)

sns.boxplot(data=df_salarios)
plt.title('Distribución de Salarios por Nivel Educativo')
plt.ylabel('Salario')
plt.show()

# Parte 8: Gráficos Avanzados

# Además de los gráficos básicos, existen muchos otros tipos de gráficos avanzados
# que pueden ser útiles dependiendo del tipo de datos que estemos visualizando.
# Algunos ejemplos incluyen gráficos de violín, gráficos de área, gráficos de radar, entre otros.