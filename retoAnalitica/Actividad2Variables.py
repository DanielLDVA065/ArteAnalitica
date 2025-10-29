import pandas as pd
data= pd.read_csv('C://Users//maeto//Documents//GitHub//ArteAnalitica//retoAnalitica//spotify.csv')

#Muestra las Variables de los datos

#Mostrar los tipos de variables
print('Tipos de variables de las columnas: ')
print(data.dtypes)

#Resumen de variables numéricas
print('Resumen de variables numericas: ')
print(data.describe())

#Resumen de variables no numéricas
print('Resumen de variables no numericas: ')
print(data.describe(include=['object']))