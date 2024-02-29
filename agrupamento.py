# -*- coding: utf-8 -*-
"""Agrupamento.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rEqqxbVqjtL4uMN_81CeWe5QyC-tN4XF
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

base_dados = pd.read_csv('wine-clustering.csv')

base_dados.info()

x = base_dados.iloc[:, 1:12].values

plt.figure(figsize=(8,7))
sns.heatmap(base_dados.corr(), annot=True, annot_kws={"fontsize":8}, cmap="flare")
plt.title("Correlation between wine features")
plt.show()

sc = StandardScaler()
base_sc = sc.fit_transform(base_dados)

pca = PCA(n_components = 2)
pca.fit(base_sc)
base_pca = pca.transform(base_sc)

medidas = []
for i in range(1, 10):
    kmeans = KMeans(n_clusters=i, init="k-means++", n_init="auto", random_state=1)
    kmeans.fit(base_pca)
    medidas.append(kmeans.inertia_)

plt.plot(range(1,10), medidas)
plt.title("Metódo Elbow")
plt.xlabel("Número de Clusters")
plt.ylabel("Medidas")
plt.show()

kmeans = KMeans(n_clusters=3, init="k-means++", n_init='auto')
kmeans.fit(base_pca)

kmeans_df = pd.DataFrame(base_pca)
kmeans_df.columns = ["Componente 1", "Componente 2"]
kmeans_df["Vinhos"] =  kmeans.labels_
kmeans_df.head()

sns.scatterplot(x=kmeans_df["Componente 2"], y=kmeans_df["Componente 1"], hue=kmeans_df["Vinhos"], palette="flare")
plt.title("Resultados do K-means")
plt.show()