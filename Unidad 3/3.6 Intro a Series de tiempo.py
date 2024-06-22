# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_process import ArmaProcess

# Configurar estilo de las gráficas
sns.set()
plt.rcParams['figure.figsize'] = (12, 6)

# Función para generar datos de series de tiempo sintéticos con tendencia y estacionalidad
def generate_realistic_time_series():
    # Parámetros
    np.random.seed(42)
    n_years = 5  # Número de años
    n_months = 12 * n_years  # Número de meses
    initial_value = 100  # Valor inicial
    trend_slope = 0.3  # Pendiente de la tendencia
    seasonal_amplitude = 20  # Amplitud de la componente estacional
    noise_std = 10  # Desviación estándar del ruido
    
    # Generar fechas mensuales
    dates = pd.date_range(start='2020-01-01', periods=n_months, freq='M')
    
    # Generar tendencia lineal creciente
    trend = initial_value + np.arange(n_months) * trend_slope
    
    # Generar componente estacional sinusoidal
    seasonal = seasonal_amplitude * np.sin(2 * np.pi * np.arange(n_months) / 12)
    
    # Generar ruido aleatorio
    noise = np.random.normal(loc=0, scale=noise_std, size=n_months)
    
    # Combinar componentes para formar la serie temporal
    time_series = trend + seasonal + noise
    
    # Crear DataFrame
    df = pd.DataFrame({'Date': dates, 'Value': time_series})
    
    # Graficar la serie de tiempo
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Value'], label='Realistic Time Series')
    plt.title('Realistic Time Series with Trend and Seasonal Components')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return df

# Función para verificar la estacionariedad de la serie de tiempo
def test_stationarity(data):
    # Realizar la prueba ADF (Augmented Dickey-Fuller) para estacionariedad
    result = adfuller(data['Value'])
    print('Results of Augmented Dickey-Fuller Test:')
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    print('Critical Values:')
    for key, value in result[4].items():
        print(f'\t{key}: {value}')
    
    # Graficar la serie de tiempo y estadísticas de media y desviación estándar móviles
    rolmean = data['Value'].rolling(window=12).mean()  # Media móvil de 12 meses
    rolstd = data['Value'].rolling(window=12).std()    # Desviación estándar móvil de 12 meses
    
    plt.figure(figsize=(12, 6))
    plt.plot(data['Value'], label='Time Series')
    plt.plot(rolmean, label='12-Month Rolling Mean', color='red')
    plt.plot(rolstd, label='12-Month Rolling Std', color='black')
    plt.title('Stationarity Analysis')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.show()
    
    return result

# Función para ajustar un modelo ARIMA a la serie de tiempo
def fit_arima_model(data):
    # Estimación de la autocorrelación y autocorrelación parcial
    plot_acf(data['Value'], lags=20, zero=False)
    plt.title('Autocorrelation')
    plt.show()
    plot_pacf(data['Value'], lags=20, zero=False)
    plt.title('Partial Autocorrelation')
    plt.show()
    
    # Ajustar un modelo ARIMA (p, d, q)
    model = ARIMA(data['Value'], order=(1, 2, 3),seasonal_order=(1, 1, 1, 12),)
    fitted_model = model.fit()
    
    # Resumen del modelo ajustado
    print(fitted_model.summary())
    
    # Diagnóstico del modelo
    fitted_model.plot_diagnostics(figsize=(12, 8))
    plt.tight_layout()
    plt.show()
    
    # Predicción futura
    forecast_steps = 12
    forecast = fitted_model.get_forecast(steps=forecast_steps)
    forecast_mean = forecast.predicted_mean
    forecast_ci = forecast.conf_int()
    
    # Graficar la serie de tiempo y la predicción futura
    plt.figure(figsize=(12, 6))
    plt.plot(data['Value'], label='Time Series')
    plt.plot(forecast_mean.index, forecast_mean, color='red', label=f'ARIMA Forecast ({forecast_steps} steps)')
    plt.fill_between(forecast_ci.index, forecast_ci.iloc[:, 0], forecast_ci.iloc[:, 1], color='pink', alpha=0.3)
    plt.title('Forecast with ARIMA Model')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

# Ejecutar las funciones principales
if __name__ == "__main__":
    # Generar y visualizar datos de serie de tiempo realista
    realistic_data = generate_realistic_time_series()
    
    # Verificar la estacionariedad de la serie de tiempo realista
    test_stationarity(realistic_data)
    
    # Ajustar un modelo ARIMA a la serie de tiempo realista
    fit_arima_model(realistic_data)
