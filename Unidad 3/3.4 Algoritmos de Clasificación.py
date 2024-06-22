# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Cargar el conjunto de datos de cáncer de mama
cancer = load_breast_cancer()
X = cancer.data  # Características
y = cancer.target  # Etiquetas

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar las características
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Función para entrenar y evaluar un modelo de clasificación
def train_and_evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)  # Entrenar el modelo
    y_pred = model.predict(X_test)  # Predecir en el conjunto de prueba
    accuracy = accuracy_score(y_test, y_pred)  # Calcular la precisión
    report = classification_report(y_test, y_pred)  # Generar el reporte de clasificación
    matrix = confusion_matrix(y_test, y_pred)  # Generar la matriz de confusión
    return accuracy, report, matrix

# Crear modelos de clasificación
models = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'Support Vector Machine': SVC(random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42)
}

# Entrenar y evaluar cada modelo
results = {}
for name, model in models.items():
    accuracy, report, matrix = train_and_evaluate_model(model, X_train, X_test, y_train, y_test)
    results[name] = {'Accuracy': accuracy, 'Classification Report': report, 'Confusion Matrix': matrix}

# Mostrar resultados
for name, result in results.items():
    print(f"=== {name} ===")
    print(f"Accuracy: {result['Accuracy']:.4f}\n")
    print("Classification Report:\n", result['Classification Report'])
    print("Confusion Matrix:\n", result['Confusion Matrix'], "\n")

# Visualización de la matriz de confusión con seaborn
plt.figure(figsize=(12, 8))
for i, (name, result) in enumerate(results.items(), 1):
    plt.subplot(2, 2, i)
    sns.heatmap(result['Confusion Matrix'], annot=True, cmap='Blues', fmt='d', cbar=False)
    plt.title(f'{name} - Confusion Matrix')
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
plt.tight_layout()
plt.show()
