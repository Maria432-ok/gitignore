# 🚗 Proyecto de Análisis y Visualización de Autos

## 1. Introducción
Este proyecto realiza la limpieza, el análisis exploratorio y la visualización de un conjunto de datos de vehículos usados (`vehicles_us.csv`). El objetivo es identificar los factores clave que influyen en el precio de venta.

## 2. Configuración y Código de Python
El código utilizado en el archivo `analisis.py` realiza lo siguiente:
1.  **Carga** de datos usando Pandas.
2.  **Limpieza** de valores faltantes (`NaN`) en columnas clave (`model_year`, `cylinders`, `odometer`, etc.) usando la mediana.
3.  **Corrección** de tipos de datos (`Dtypes`) para asegurar la precisión numérica y temporal.
4.  **Generación** de dos gráficos clave (Histograma y Gráfico de Dispersión) usando Plotly Express.

---

## 3. Conclusiones del Análisis Visual

### 3.1 Histograma (Precio vs. Condición)
**Análisis:** El histograma muestra que los anuncios más comunes son para vehículos en condiciones 'excelente' y 'buena', que forman la base del mercado de segunda mano. La distribución de precios está fuertemente correlacionada con la condición: los vehículos 'nuevos' tienen precios muy altos, mientras que los vehículos en condición 'salvamento' se agrupan en el rango de precios más bajo.

**Conclusión:** La condición del vehículo es el factor cualitativo más importante que influye en el precio de venta, lo que confirma las tendencias de depreciación esperadas en el mercado de vehículos usados.

### 3.2 Gráfico de Dispersión (Kilometraje vs. Precio)
**Análisis:**
Se observa una clara **correlación negativa** entre el kilometraje (`odometer`) y el precio de venta. A medida que el valor del kilometraje aumenta (moviéndose hacia la derecha), la concentración de puntos se desplaza hacia abajo (precios más bajos), lo que indica una depreciación constante.

**Conclusión:** El kilometraje es un factor cuantitativo clave de depreciación. Es un buen predictor del precio final, y los precios son menos dispersos (más predecibles) en el rango de kilometraje más bajo.

---

