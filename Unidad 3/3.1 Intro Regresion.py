import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.use('Agg')
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. Introduction to Regression
print("1. Regresion")
print("y = mx +b")

# 2. Simple Linear Regression
print("\n2. Reg Simple")
np.random.seed(0)
X = np.random.rand(100, 1)
y = 2 + 3 * X + np.random.randn(100, 1) * 0.1

model = LinearRegression()
model.fit(X, y)

print(f"Intercept: {model.intercept_[0]:.2f}")
print(f"Slope: {model.coef_[0][0]:.2f}")

plt.scatter(X, y)
plt.plot(X, model.predict(X), color='red')
plt.title("Regresion simple")
plt.show()


# 3. Reg Multiple
print("\n3. Reg Multiple")
X_multi = np.random.rand(100, 2)
y_multi = 1 + 2*X_multi[:, 0] + 3*X_multi[:, 1] + np.random.randn(100) * 0.1

model_multi = LinearRegression()
model_multi.fit(X_multi, y_multi)

print(f"Intercept: {model_multi.intercept_:.2f}")
print(f"Coefficients: {model_multi.coef_}")


# 4. Reg Polinomial 
print("\n4. Regresion polinomial")
X_poly = np.linspace(0, 1, 100).reshape(-1, 1)
y_poly = 1 + 2*X_poly + 3*X_poly**2 + np.random.randn(100, 1) * 0.1

poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly_features = poly_features.fit_transform(X_poly)

model_poly = LinearRegression()
model_poly.fit(X_poly_features, y_poly)

plt.scatter(X_poly, y_poly)
plt.plot(X_poly, model_poly.predict(X_poly_features), color='red')
plt.title("Reg Polinomial")
plt.show()

# 5. Regularization: Ridge Regression
print("\n5. Regularization: Ridge ")
X_train, X_test, y_train, y_test = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)

ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

y_pred_ridge = ridge.predict(X_test)
print(f"Ridge R2 Score: {r2_score(y_test, y_pred_ridge):.2f}")

# 6. Regularization: Lasso Regression
print("\n6. Regularization: Lasso")
lasso = Lasso(alpha=1.0)
lasso.fit(X_train, y_train)

y_pred_lasso = lasso.predict(X_test)
print(f"Lasso R2 Score: {r2_score(y_test, y_pred_lasso):.2f}")

# 7. Evaluacion
print("\n7. Model Evaluation")
y_pred = model_multi.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R2 Score: {r2:.2f}")

# 8. Residual Analysis
print("\n8. Residual Analysis")
residuals = y_test - y_pred
plt.scatter(y_pred, residuals)
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()

# 9. Feature Importance
print("\n9. Feature Importance")
feature_importance = abs(model_multi.coef_)
for i, importance in enumerate(feature_importance):
    print(f"Feature {i+1} importance: {importance:.2f}")

# 10. Cross-validation (simplified example)
print("\n10. Cross-validation")
from sklearn.model_selection import cross_val_score

cv_scores = cross_val_score(model_multi, X_multi, y_multi, cv=5)
print(f"Cross-validation scores: {cv_scores}")
print(f"Mean CV score: {np.mean(cv_scores):.2f}")