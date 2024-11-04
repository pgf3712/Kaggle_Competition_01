# 🖥️💰 Predicción de Precios de Portátiles - Kaggle Competition

¡Bienvenid@ a mi proyecto de predicción de precios de portátiles en la competencia de Kaggle! 🚀 Aquí, aplico mis conocimientos de Machine Learning para desarrollar un modelo capaz de predecir el precio de los portátiles basándome en sus características y prestaciones.

___

## 📝 Enunciado de la Competencia

Nuestro jefe estaba buscando una solución automatizada para asignar precios a los portátiles de la tienda "Cositas-Markt". Sin embargo, las máquinas se habían ido de vacaciones y nos lo pidió a nosotr@s... 💥🪓🔪

### 🎯 Objetivo
Desarrollar un modelo de predicción de precios de portátiles a partir de sus especificaciones, de forma que la tienda pueda lanzar productos con precios competitivos en el mercado.

## 📊 Dataset
El dataset proporcionado contiene los siguientes campos:

1. **Company**: Marca del portátil (e.g., Dell, HP, Apple)
2. **Product**: Marca y modelo
3. **TypeName**: Tipo (e.g., Notebook, Ultrabook, Gaming)
4. **Inches**: Tamaño de la pantalla en pulgadas
5. **ScreenResolution**: Resolución de la pantalla
6. **Cpu**: Unidad Central de Procesamiento (CPU)
7. **Ram**: Memoria RAM
8. **Memory**: Capacidad de almacenamiento (HDD/SSD)
9. **GPU**: Unidad de Procesamiento Gráfico
10. **OpSys**: Sistema operativo
11. **Weight**: Peso del portátil
12. **Price_euros**: Precio en euros (variable objetivo)

## 🧪 Evaluación
El rendimiento del modelo se evaluará mediante el **Error Absoluto Medio (MAE)**. El archivo de envío debe seguir el formato proporcionado en `sample_submission.csv`.

## 🚀 Enfoque de Solución
Para abordar esta competencia, aplicamos un pipeline de limpieza y transformación de datos, que incluye:

- **Preprocesamiento de columnas**: Normalización y conversión de datos como peso, RAM y resolución.
- **Extracción de características**: Clasificación de procesadores, almacenamiento, tarjetas gráficas, etc.
- **Visualización**: Creación de mapas de correlación y gráficos para entender mejor la relación entre características.

### 🔧 Funciones y Herramientas
Algunas de las funciones principales incluyen:
- `pasar_a_limpito_ds(df)`: Limpia y transforma el dataset.
- `crear_mapa_de_correlacion(df)`: Genera un mapa de correlación para visualizar relaciones entre características numéricas.

## 🔍 Resultados
El modelo entrenado busca minimizar el MAE y ayudar en la correcta estimación de precios para la tienda "Cositas-Markt".

## 🤝 Contribuciones
¡Contribuciones, ideas y sugerencias son bienvenidas! Si quieres colaborar, no dudes en abrir un *issue* o enviar un *pull request*.

## 📫 Contacto
Si tienes preguntas o quieres saber más sobre el proyecto, puedes contactarme a través de GitHub o en mis redes sociales.

---

¡Gracias por visitar mi proyecto! 😊✨
