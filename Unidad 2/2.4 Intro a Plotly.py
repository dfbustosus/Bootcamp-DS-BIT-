# Parte 1: Instalación y Configuración

# Lo primero que necesitamos hacer es instalar Plotly.
# Puedes instalar Plotly utilizando pip:
#!python -m pip install -q plotly
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Parte 2: Gráfico de Líneas Interactivo

# Empezaremos creando un gráfico de líneas interactivo.
# Generamos algunos datos aleatorios para el eje x y el eje y.
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Creamos la figura y añadimos un trazado de línea.
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='sin(x)'))
# Personalizamos el diseño del gráfico.
fig.update_layout(title='Gráfico de Líneas Interactivo',
                  xaxis_title='Eje X',
                  yaxis_title='Eje Y')

# Mostramos el gráfico interactivo.
fig.show()


# Parte 3: Gráfico de Barras Interactivo

# Ahora crearemos un gráfico de barras interactivo.
# Generamos algunos datos para las barras.
categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]

# Creamos la figura y añadimos un trazado de barras.
fig = go.Figure()
fig.add_trace(go.Bar(x=categorias, y=valores))

# Personalizamos el diseño del gráfico.
fig.update_layout(title='Gráfico de Barras Interactivo',
                  xaxis_title='Categorías',
                  yaxis_title='Valores')

# Mostramos el gráfico interactivo.
fig.show()

# Parte 4: Gráfico de Pastel Interactivo

# Continuaremos con un gráfico de pastel interactivo.
# Generamos algunos datos para el pastel.
fuentes = ['A', 'B', 'C', 'D']
porcentajes = [25, 30, 20, 25]

# Creamos la figura y añadimos un trazado de pastel.
fig = go.Figure()
fig.add_trace(go.Pie(labels=fuentes, values=porcentajes))

# Personalizamos el diseño del gráfico.
fig.update_layout(title='Gráfico de Pastel Interactivo')

# Mostramos el gráfico interactivo.
fig.show()

# Parte 5: Gráfico de Dispersión Interactivo

# Ahora crearemos un gráfico de dispersión interactivo.
# Generamos algunos datos para los puntos.
x = np.random.rand(100)
y = np.random.rand(100)

# Creamos la figura y añadimos un trazado de dispersión.
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='markers'))

# Personalizamos el diseño del gráfico.
fig.update_layout(title='Gráfico de Dispersión Interactivo')

# Mostramos el gráfico interactivo.
fig.show()

# Parte 6: Personalización Avanzada

np.random.seed(0)
dates = pd.date_range(start='2022-01-01', end='2022-12-31')
data1 = np.random.randn(len(dates)).cumsum()
data2 = np.random.randn(len(dates)).cumsum()

# Creamos la figura y añadimos trazados para cada serie
fig = go.Figure()
fig.add_trace(go.Scatter(x=dates, y=data1, mode='lines', name='Serie 1'))
fig.add_trace(go.Scatter(x=dates, y=data2, mode='lines', name='Serie 2'))

# Personalizamos el diseño del gráfico con todas las herramientas estéticas disponibles
fig.update_layout(
    title='Gráfico de Series de Tiempo con Múltiples Series',
    xaxis=dict(
        title='Fecha',
        showgrid=True,
        showline=True,
        showticklabels=True,
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='black'
        ),
        tickformat='%Y-%m-%d',  # Formato de las fechas en el eje x
        tickangle=45,  # Ángulo de inclinación de las etiquetas del eje x
        tickmode='auto',  # Modo automático para las marcas del eje x
        ticklen=10,  # Longitud de las marcas del eje x
        tickwidth=2,  # Ancho de las marcas del eje x
    ),
    yaxis=dict(
        title='Valor',
        showgrid=True,
        showline=True,
        showticklabels=True,
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='black'
        ),
        ticklen=10,  # Longitud de las marcas del eje y
        tickwidth=2,  # Ancho de las marcas del eje y
    ),
    plot_bgcolor='white',  # Color de fondo del gráfico
    paper_bgcolor='white',  # Color de fondo del papel
    legend=dict(
        title='Series',  # Título de la leyenda
        font=dict(
            family='Arial',
            size=12,
            color='black'
        ),
        bgcolor='white',  # Color de fondo de la leyenda
        bordercolor='black',  # Color del borde de la leyenda
        borderwidth=1,  # Ancho del borde de la leyenda
    ),
    margin=dict(
        l=50,  # Margen izquierdo
        r=50,  # Margen derecho
        b=50,  # Margen inferior
        t=80,  # Margen superior
        pad=4,  # Espacio entre el gráfico y el borde del contenedor
    ),
)

fig.show()
