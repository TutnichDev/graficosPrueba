import pandas as pd
import altair as alt

ruta_archivo = "C:/Documentos/n76359/Maestria/Python/pruebaGraf/dataset.csv"

datos = pd.read_csv(ruta_archivo, sep=';')

grafico = alt.Chart(datos).mark_bar().encode(
    x='Categoría',  # Eje X: columna "Categoría"
    y='Periodo'       # Eje Y: columna "Valor"
)

grafico.show()  # Mostrar el gráfico


print(datos.head)