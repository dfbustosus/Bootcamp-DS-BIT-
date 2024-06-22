import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.svm import SVC, SVR
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report
from sklearn.datasets import make_classification, make_regression

np.random.seed(42)

print("Aprendizaje Supervisado")

# Funciones auxiliares
def evaluate_regression(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"Error Cuadrático Medio: {mse:.4f}")
    print(f"R2 Score: {r2:.4f}")

def evaluate_classification(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    print(f"Precisión: {accuracy:.4f}")
    print("Informe de Clasificación:")
    print(classification_report(y_true, y_pred))

# 1. Regresión Lineal
print("\n1. Regresión Lineal")
X, y = make_regression(n_samples=100, n_features=1, noise=0.1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Resultados de Regresión Lineal:")
evaluate_regression(y_test, y_pred)

plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred, color='red')
plt.title("Regresión Lineal")
plt.savefig('regresion_lineal.png')
plt.close()

# 2. Regresión Polinómica
print("\n2. Regresión Polinómica")
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
X_train_poly, X_test_poly, y_train, y_test = train_test_split(X_poly, y, test_size=0.2)

model_poly = LinearRegression()
model_poly.fit(X_train_poly, y_train)
y_pred_poly = model_poly.predict(X_test_poly)

print("Resultados de Regresión Polinómica:")
evaluate_regression(y_test, y_pred_poly)

# 3. Regresión Ridge (L2)
print("\n3. Regresión Ridge")
model_ridge = Ridge(alpha=1.0)
model_ridge.fit(X_train, y_train)
y_pred_ridge = model_ridge.predict(X_test)

print("Resultados de Regresión Ridge:")
evaluate_regression(y_test, y_pred_ridge)

# 4. Regresión Lasso (L1)
print("\n4. Regresión Lasso")
model_lasso = Lasso(alpha=1.0)
model_lasso.fit(X_train, y_train)
y_pred_lasso = model_lasso.predict(X_test)

print("Resultados de Regresión Lasso:")
evaluate_regression(y_test, y_pred_lasso)

# 5. Árbol de Decisión (Regresión)
print("\n5. Árbol de Decisión (Regresión)")
model_tree = DecisionTreeRegressor(max_depth=3)
model_tree.fit(X_train, y_train)
y_pred_tree = model_tree.predict(X_test)

print("Resultados del Árbol de Decisión (Regresión):")
evaluate_regression(y_test, y_pred_tree)

# 6. Random Forest (Regresión)
print("\n6. Random Forest (Regresión)")
model_rf = RandomForestRegressor(n_estimators=100, max_depth=3)
model_rf.fit(X_train, y_train)
y_pred_rf = model_rf.predict(X_test)

print("Resultados de Random Forest (Regresión):")
evaluate_regression(y_test, y_pred_rf)

# 7. Gradient Boosting (Regresión)
print("\n7. Gradient Boosting (Regresión)")
model_gb = GradientBoostingRegressor(n_estimators=100, max_depth=3)
model_gb.fit(X_train, y_train)
y_pred_gb = model_gb.predict(X_test)

print("Resultados de Gradient Boosting (Regresión):")
evaluate_regression(y_test, y_pred_gb)

# 8. Support Vector Regression (SVR)
print("\n8. Support Vector Regression (SVR)")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model_svr = SVR(kernel='rbf')
model_svr.fit(X_train_scaled, y_train)
y_pred_svr = model_svr.predict(X_test_scaled)

print("Resultados de SVR:")
evaluate_regression(y_test, y_pred_svr)

# 9. K-Nearest Neighbors (Regresión)
print("\n9. K-Nearest Neighbors (Regresión)")
model_knn = KNeighborsRegressor(n_neighbors=5)
model_knn.fit(X_train, y_train)
y_pred_knn = model_knn.predict(X_test)

print("Resultados de KNN (Regresión):")
evaluate_regression(y_test, y_pred_knn)

# Ahora pasamos a problemas de clasificación
print("\nProblemas de Clasificación")

# Generamos datos para clasificación
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_classes=2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 10. Regresión Logística
print("\n10. Regresión Logística")
model_log = LogisticRegression()
model_log.fit(X_train, y_train)
y_pred_log = model_log.predict(X_test)

print("Resultados de Regresión Logística:")
evaluate_classification(y_test, y_pred_log)

# 11. Árbol de Decisión (Clasificación)
print("\n11. Árbol de Decisión (Clasificación)")
model_tree_clf = DecisionTreeClassifier(max_depth=3)
model_tree_clf.fit(X_train, y_train)
y_pred_tree_clf = model_tree_clf.predict(X_test)

print("Resultados del Árbol de Decisión (Clasificación):")
evaluate_classification(y_test, y_pred_tree_clf)

# 12. Random Forest (Clasificación)
print("\n12. Random Forest (Clasificación)")
model_rf_clf = RandomForestClassifier(n_estimators=100, max_depth=3)
model_rf_clf.fit(X_train, y_train)
y_pred_rf_clf = model_rf_clf.predict(X_test)

print("Resultados de Random Forest (Clasificación):")
evaluate_classification(y_test, y_pred_rf_clf)

# 13. Gradient Boosting (Clasificación)
print("\n13. Gradient Boosting (Clasificación)")
model_gb_clf = GradientBoostingClassifier(n_estimators=100, max_depth=3)
model_gb_clf.fit(X_train, y_train)
y_pred_gb_clf = model_gb_clf.predict(X_test)

print("Resultados de Gradient Boosting (Clasificación):")
evaluate_classification(y_test, y_pred_gb_clf)

# 14. Support Vector Machine (SVM)
print("\n14. Support Vector Machine (SVM)")
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model_svm = SVC(kernel='rbf')
model_svm.fit(X_train_scaled, y_train)
y_pred_svm = model_svm.predict(X_test_scaled)

print("Resultados de SVM:")
evaluate_classification(y_test, y_pred_svm)

# 15. K-Nearest Neighbors (Clasificación)
print("\n15. K-Nearest Neighbors (Clasificación)")
model_knn_clf = KNeighborsClassifier(n_neighbors=5)
model_knn_clf.fit(X_train, y_train)
y_pred_knn_clf = model_knn_clf.predict(X_test)

print("Resultados de KNN (Clasificación):")
evaluate_classification(y_test, y_pred_knn_clf)

# 16. Validación Cruzada
print("\n16. Validación Cruzada")
scores = cross_val_score(model_rf, X, y, cv=5)
print(f"Puntuaciones de validación cruzada: {scores}")
print(f"Media de validación cruzada: {scores.mean():.4f}")
