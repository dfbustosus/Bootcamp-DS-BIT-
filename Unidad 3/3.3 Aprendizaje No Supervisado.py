# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_moons
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import warnings
warnings.filterwarnings("ignore")

# Configuración de los datos sintéticos
n_samples = 1000
random_state = 42

# Generar datos sintéticos para clustering y reducción de dimensionalidad
X_cluster, y_cluster = make_blobs(n_samples=n_samples, centers=4, cluster_std=0.5, random_state=random_state)
X_moons, y_moons = make_moons(n_samples=n_samples, noise=0.1, random_state=random_state)

# Ejemplo 1: Clustering con K-Means
def kmeans_clustering(X):
    kmeans = KMeans(n_clusters=4, random_state=random_state)
    y_kmeans = kmeans.fit_predict(X)
    return y_kmeans

# Ejemplo 2: Clustering con DBSCAN
def dbscan_clustering(X):
    dbscan = DBSCAN(eps=0.3, min_samples=10)
    y_dbscan = dbscan.fit_predict(X)
    return y_dbscan

# Ejemplo 3: Clustering jerárquico con Agglomerative Clustering
def hierarchical_clustering(X):
    agglo = AgglomerativeClustering(n_clusters=4)
    y_agglo = agglo.fit_predict(X)
    return y_agglo

# Ejemplo 4: Reducción de dimensionalidad con PCA
def pca_reduction(X):
    pca = PCA(n_components=2, random_state=random_state)
    X_pca = pca.fit_transform(X)
    return X_pca

# Ejemplo 5: Reducción de dimensionalidad con t-SNE
def tsne_reduction(X):
    tsne = TSNE(n_components=2, random_state=random_state)
    X_tsne = tsne.fit_transform(X)
    return X_tsne

# Función para visualizar resultados
def plot_results(X, y, title):
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', s=50, alpha=0.7)
    plt.title(title)
    plt.xlabel('Característica 1')
    plt.ylabel('Característica 2')

    plt.subplot(1, 2, 2)
    plt.title('Datos originales')
    plt.scatter(X[:, 0], X[:, 1], c='gray', s=20, alpha=0.5)
    plt.xlabel('Característica 1')
    plt.ylabel('Característica 2')

    plt.tight_layout()
    plt.show()

# Ejemplo de uso: Clustering con K-Means en datos sintéticos de blobs
y_kmeans = kmeans_clustering(X_cluster)
plot_results(X_cluster, y_kmeans, 'Clustering con K-Means')

# Ejemplo de uso: Reducción de dimensionalidad con t-SNE en datos sintéticos de moons
X_tsne = tsne_reduction(X_moons)
plot_results(X_tsne, y_moons, 'Reducción de dimensionalidad con t-SNE')

# Ejemplo de uso: Clustering jerárquico en datos sintéticos de blobs
y_agglo = hierarchical_clustering(X_cluster)
plot_results(X_cluster, y_agglo, 'Clustering jerárquico con Agglomerative Clustering')

# Ejemplo de uso: Reducción de dimensionalidad con PCA en datos sintéticos de moons
X_pca = pca_reduction(X_moons)
plot_results(X_pca, y_moons, 'Reducción de dimensionalidad con PCA')
