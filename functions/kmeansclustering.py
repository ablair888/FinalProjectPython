import statistics
import plotnine
import numpy
from plotnine import *
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

url = 'https://raw.githubusercontent.com/ablair00/FinalProject/main/data/5937P.csv'
df = pd.read_csv(url)

kcluster_df = df[['danceability','energy','key','loudness', 'mode','speechiness','instrumentalness','liveness','valence','tempo','duration_ms','time_signature']] #these columns should match names of your columns


def numberofclusters(dataset):
    wcss = []
    for i in range(1,11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(dataset)
        wcss.append(kmeans.inertia_)

    plt.plot(range(1,11), wcss)
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()

numberofclusters(kcluster_df)

def kmeansplot(dataset):
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(dataset)
    y_kmeans = kmeans.predict(dataset)

    plt.scatter(dataset['duration_ms'], dataset['energy'], c=y_kmeans, s=50)
    plt.show()

kmeansplot(kcluster_df)
