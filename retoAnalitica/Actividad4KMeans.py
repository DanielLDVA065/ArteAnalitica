import pandas as pd
import matplotlib.pyplot as mat
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import numpy as np

datos= pd.read_csv('C://Users//maeto//Documents//GitHub//ArteAnalitica//retoAnalitica//Facebook_Marketplace_data.csv')
#Variables numericas
numerico= datos.select_dtypes(include='number')
numerico = numerico.dropna()
datos = datos.loc[numerico.index]

# Graficar método del codo
inertia = []
K_range = range(1, 11)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(numerico)
    inertia.append(kmeans.inertia_)
mat.figure(figsize=(8,5))
mat.plot(K_range, inertia, marker='o')
mat.xlabel("Número de clusters")
mat.ylabel("Inercia")
mat.title("Método del codo para determinar K óptimo")
mat.show()

#Dinstancias entre centroides
distancias = cdist(kmeans.cluster_centers_, kmeans.cluster_centers_)
print("Distancias entre centroides: ")
print(np.round(distancias, 2))

kmeans = KMeans(n_clusters=3, random_state=0)
#Entrenar el modelo
datos['cluster'] = kmeans.fit_predict(numerico)
print(kmeans.cluster_centers_)

#Visualizacion de los clusters
mat.figure(figsize=(8,6))
mat.scatter(datos['num_comments'], datos['num_shares'], c=datos['cluster'], cmap='viridis')
mat.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], 
            c='red', marker='x', s=200, label='Centroides')
mat.title('Clustering con K-Means')
mat.xlabel('num_comments')
mat.ylabel('num_shares')
mat.legend()
mat.show()

