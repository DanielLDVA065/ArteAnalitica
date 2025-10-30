import pandas as pd
import matplotlib.pyplot as mat
import seaborn as sea
#Modo interactivo
mat.ion()

datos= pd.read_csv('C://Users//maeto//Documents//GitHub//ArteAnalitica//retoAnalitica//Facebook_Marketplace_data.csv')
numerico= datos.select_dtypes(include='number')

#Diagrama de cajas y bigotes
sea.boxplot(data=numerico)
mat.title('Cajas y bigotes')
mat.show(block=True)

#Histograma del numero de reacciones
sea.histplot(numerico['num_reactions'], kde=True,)
mat.title('Histograma de numero de reacciones')
mat.show(block=True)

#Mapa de calor
correlacion = numerico.corr(numeric_only=True)
sea.heatmap(correlacion, annot=True, cmap="coolwarm", fmt=".2f")
mat.title('Mapa de calor')
mat.show(block=True)
