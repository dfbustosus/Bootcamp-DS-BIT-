# Parte 1: Instalación y Configuración

# Antes que nada, asegúrate de tener Seaborn instalado.
# Puedes instalarlo fácilmente con pip:
# pip install seaborn

# Ahora, vamos a importar Seaborn junto con otras librerías necesarias.
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Parte 2: Cargando un Conjunto de Datos

# Seaborn viene con varios conjuntos de datos integrados que podemos utilizar para practicar.
# Por ejemplo, podemos cargar el conjunto de datos "tips" que contiene información sobre propinas en un restaurante.
tips_data = sns.load_dataset("tips")

# Veamos las primeras filas del conjunto de datos para entender su estructura.
print(tips_data.head())

# Parte 3: Gráficos Básicos

# Empezaremos con un gráfico básico utilizando el método sns.scatterplot().
# Vamos a graficar la relación entre el total de la cuenta y la propina.
sns.scatterplot(data=tips_data, x="total_bill", y="tip")
plt.title("Total de la Cuenta vs Propina")
plt.xlabel("Total de la Cuenta")
plt.ylabel("Propina")
plt.show()

# Parte 4: Personalización de Gráficos

# Seaborn nos permite personalizar nuestros gráficos de manera sencilla.
# Por ejemplo, podemos añadir colores diferenciando el sexo de los comensales.
sns.scatterplot(data=tips_data, x="total_bill", y="tip", hue="sex")
plt.title("Total de la Cuenta vs Propina por Sexo")
plt.xlabel("Total de la Cuenta")
plt.ylabel("Propina")
plt.show()

# Parte 5: Gráficos de Distribución

# Los gráficos de distribución nos permiten visualizar la distribución de un conjunto de datos.
# Vamos a crear un histograma de la distribución de las propinas.
sns.histplot(data=tips_data, x="tip", bins=10, kde=True)
plt.title("Distribución de Propinas")
plt.xlabel("Propina")
plt.ylabel("Frecuencia")
plt.show()

# Parte 6: Gráficos Categóricos

# Seaborn también nos permite crear gráficos categóricos, como los gráficos de barras.
# Vamos a crear un gráfico de barras que muestre la cantidad de propinas según el día de la semana.
sns.barplot(data=tips_data, x="day", y="tip")
plt.title("Promedio de Propina por Día")
plt.xlabel("Día de la Semana")
plt.ylabel("Promedio de Propina")
plt.show()

# Parte 7: Mapas de Calor

# Los mapas de calor nos permiten visualizar la correlación entre variables en un conjunto de datos.
# Vamos a crear un mapa de calor para el conjunto de datos tips_data.
correlation_matrix = tips_data.drop(columns=['sex','smoker','day','time']).corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Mapa de Calor de Correlación")
plt.show()

# Parte 8: Gráficos de Pares

# Los gráficos de pares nos permiten explorar las relaciones entre múltiples variables.
# Vamos a crear un gráfico de pares para el conjunto de datos tips_data.
sns.pairplot(tips_data)
#plt.title("Gráfico de Pares del Conjunto de Datos Tips")
plt.show()

# Parte 9: Personalización Avanzada

# Seaborn nos ofrece muchas opciones de personalización avanzada para nuestros gráficos.
# Por ejemplo, podemos cambiar el estilo de los gráficos.
sns.set_style("darkgrid")

# También podemos ajustar el tamaño de los gráficos.
plt.figure(figsize=(8, 6))

# Y podemos cambiar la paleta de colores.
sns.scatterplot(data=tips_data, x="total_bill", y="tip", hue="day", palette="Set2")
plt.title("Total de la Cuenta vs Propina por Día")
plt.xlabel("Total de la Cuenta")
plt.ylabel("Propina")
plt.show()