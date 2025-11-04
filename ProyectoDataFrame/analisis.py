import pandas as pd
import plotly.express as px

# --- PASO 1 & 2: CARGA, LIMPIEZA Y CORRECCIÓN DE DATOS ---
try:
    # Carga del archivo CSV
    df = pd.read_csv('vehicles_us.csv')
    
    # Llenado de nulos (Imputación con Mediana/Cero)
    df['model_year'].fillna(df['model_year'].median(), inplace=True)
    df['cylinders'].fillna(df['cylinders'].median(), inplace=True)
    df['odometer'].fillna(df['odometer'].median(), inplace=True)
    df['is_4wd'].fillna(0, inplace=True)
    df['paint_color'].fillna('desconocido', inplace=True)

    # Conversión de tipos de datos
    df['model_year'] = df['model_year'].astype(int)
    df['cylinders'] = df['cylinders'].astype(int)
    df['is_4wd'] = df['is_4wd'].astype(int)
    df['date_posted'] = pd.to_datetime(df['date_posted'])
    
    # --- PASO 3: VISUALIZACIÓN DE DATOS ---
    
    print("✅ Datos listos. Generando gráficos...")

    # VISUALIZACIÓN 1: Histograma de Condición vs. Precio
    fig_hist = px.histogram(df, 
                            x="price", 
                            color="condition",
                            title="Distribución de Precio por Condición del Vehículo",
                            labels={'price':'Precio', 'condition':'Condición'})
    fig_hist.show() 
    
    # VISUALIZACIÓN 2: Gráfico de Dispersión (Scatter) de Kilometraje vs. Precio
    fig_scatter = px.scatter(df, 
                             x="odometer", 
                             y="price", 
                             title="Relación entre Kilometraje y Precio",
                             labels={'odometer':'Kilometraje (Millas)', 'price':'Precio'},
                             opacity=0.5, 
                             template="plotly_white")
    fig_scatter.show() 

except Exception as e:
    print(f"❌ Ocurrió un error al cargar o visualizar: {e}")