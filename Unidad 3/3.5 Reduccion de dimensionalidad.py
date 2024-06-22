# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data  # Características
y = iris.target  # Etiquetas
target_names = iris.target_names  # Nombres de las clases

# Normalizar las características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Función para graficar la varianza explicada por cada componente principal
def plot_variance_explained(pca):
    plt.figure(figsize=(10, 6))
    plt.bar(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_, alpha=0.5, align='center')
    plt.step(range(1, len(pca.explained_variance_ratio_) + 1), np.cumsum(pca.explained_variance_ratio_), where='mid')
    plt.xlabel('Número de Componentes Principales')
    plt.ylabel('Varianza Explicada')
    plt.title('Varianza Explicada por Componentes Principales')
    plt.xticks(range(1, len(pca.explained_variance_ratio_) + 1))
    plt.show()

# Función para aplicar PCA y visualizar los resultados
def apply_pca(X_scaled, n_components):
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)
    
    # Graficar la varianza explicada
    plot_variance_explained(pca)
    
    # Graficar los datos reducidos a 2D
    plt.figure(figsize=(10, 8))
    for i, target_name in zip(range(len(target_names)), target_names):
        plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], label=target_name)
    plt.title('PCA de Iris Dataset')
    plt.xlabel('Componente Principal 1')
    plt.ylabel('Componente Principal 2')
    plt.legend()
    plt.show()

# Función para aplicar t-SNE y visualizar los resultados
def apply_tsne(X_scaled):
    tsne = TSNE(n_components=2, random_state=42)
    X_tsne = tsne.fit_transform(X_scaled)
    
    # Graficar los datos reducidos a 2D
    plt.figure(figsize=(10, 8))
    for i, target_name in zip(range(len(target_names)), target_names):
        plt.scatter(X_tsne[y == i, 0], X_tsne[y == i, 1], label=target_name)
    plt.title('t-SNE de Iris Dataset')
    plt.xlabel('Componente t-SNE 1')
    plt.ylabel('Componente t-SNE 2')
    plt.legend()
    plt.show()

# Aplicar PCA y t-SNE al conjunto de datos Iris
apply_pca(X_scaled, n_components=4)
apply_tsne(X_scaled)
