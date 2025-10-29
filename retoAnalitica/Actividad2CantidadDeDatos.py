import pandas as pd
data= pd.read_csv('C://Users//maeto//Documents//GitHub//ArteAnalitica//retoAnalitica//spotify.csv')

#Codigo que muestra la cantidad de datos

#Columnas
print('Columnas del archivo: ')
print(data.columns)
#(Filas, Columnas)
print('Dimensiones del archivo: ')
print(data.shape)
#Total de elementos
print('Total de elementos del archivo: ')
print(data.size)