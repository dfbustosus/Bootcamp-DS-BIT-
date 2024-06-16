# Parte 1: Instalación y configuración

# Primero, asegúrate de tener Matplotlib instalado. Puedes instalarlo usando pip:
#!python -m pip install -q matplotlib
# Importamos la librería
import matplotlib.pyplot as plt
# Parte 2: Creación de gráficos básicos
# Empezamos con un gráfico de líneas simple.
import numpy as np

# Creamos algunos datos para graficar
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Creamos el gráfico
plt.plot(x, y)
plt.title('Gráfico de Línea')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()


# Parte 3: Personalización de gráficos

# Podemos personalizar nuestros gráficos con diferentes estilos y opciones.
plt.plot(x, y, label='Seno', color='blue', linestyle='--')
plt.title('Gráfico de Línea Personalizado')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid(True)
plt.show()


# Parte 4: Gráficos de dispersión

# Para gráficos de dispersión, usamos plt.scatter.
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='red')
plt.title('Gráfico de Dispersión')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()

# Parte 5: Histogramas

# Los histogramas son útiles para mostrar distribuciones de datos.
data = np.random.randn(1000)

plt.hist(data, bins=30, alpha=0.5, color='r')
plt.title('Histograma')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()


# Parte 6: Gráficos de barras

# Los gráficos de barras son útiles para comparar diferentes categorías.
categorias = ['A', 'B', 'C', 'D']
valores = [3, 7, 5, 12]

plt.bar(categorias, valores, color=['blue', 'green', 'red', 'purple'])
plt.title('Gráfico de Barras')
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.show()

# Parte 7: Gráficos de pastel

# Los gráficos de pastel son útiles para mostrar proporciones.
tamaños = [15, 30, 45, 10]
etiquetas = ['Frodo', 'Sam', 'Gandalf', 'Aragorn']
colores = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

plt.pie(tamaños, labels=etiquetas, colors=colores, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Gráfico de Pastel')
plt.axis('equal')  # Para que el gráfico sea circular.
plt.show()

# Parte 8: Subplots

# Podemos crear múltiples gráficos en una sola figura usando subplots.
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
ax1.plot(x, y1, 'r')
ax1.set_title('Seno')
ax2.plot(x, y2, 'b')
ax2.set_title('Coseno')
plt.tight_layout()
plt.show()


# Parte 9: Guardar gráficos

# Podemos guardar nuestros gráficos en archivos.
plt.plot(x, y1, label='Seno', color='blue')
plt.title('Gráfico para Guardar')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.savefig('grafico_seno.png')
plt.show()


# Parte 10: Consejos avanzados

# 1. Uso de estilos predeterminados
plt.style.use('ggplot')
plt.plot(x, y1, label='Seno')
plt.plot(x, y2, label='Coseno')
plt.title('Uso de Estilos')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.show()

# 2. Creación de gráficos interactivos con Jupyter Notebooks
# Si usas Jupyter Notebooks, puedes crear gráficos interactivos con %matplotlib notebook.
# Aquí hay un ejemplo rápido:
# %matplotlib notebook
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.show()