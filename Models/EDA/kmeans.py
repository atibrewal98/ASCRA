import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from kneed import KneeLocator
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
from sklearn.metrics import adjusted_rand_score
import collections

def getKmeans(df):
    df = df[df.columns[:47]]
    X = df.values
    
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(X)

    kmeans = KMeans(
        init="random",
        n_clusters=3,
        n_init=10,
        max_iter=300,
        random_state=42
    )
    kmeans.fit(scaled_features)
    
    print("Inertia: ", kmeans.inertia_)
    print("Centers: ", kmeans.cluster_centers_)
    print("Iteration: ", kmeans.n_iter_)
    print("Labels: ", collections.Counter(kmeans.labels_))
    

def getElbow(df):
    df = df[df.columns[:47]]
    X = df.values
    
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(X)
    
    kmeans_kwargs = {
        "init": "random",
        "n_init": 10,
        "max_iter": 300,
        "random_state": 42,
    }
    
    # A list holds the SSE values for each k
    sse = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
        kmeans.fit(scaled_features)
        sse.append(kmeans.inertia_)
    
    plt.style.use("fivethirtyeight")
    plt.plot(range(1, 11), sse)
    plt.xticks(range(1, 11))
    plt.xlabel("Number of Clusters")
    plt.ylabel("SSE")
    plt.show()
     
    kl = KneeLocator(
        range(1, 11), sse, curve="convex", direction="decreasing"
    )

    print("Elbow:", kl.elbow)
    
    # A list holds the silhouette coefficients for each k
    silhouette_coefficients = []
    
    # Notice you start at 2 clusters for silhouette coefficient
    for k in range(2, 11):
        kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
        kmeans.fit(scaled_features)
        score = silhouette_score(scaled_features, kmeans.labels_)
        silhouette_coefficients.append(score)
    
    plt.style.use("fivethirtyeight")
    plt.plot(range(2, 11), silhouette_coefficients)
    plt.xticks(range(2, 11))
    plt.xlabel("Number of Clusters")
    plt.ylabel("Silhouette Coefficient")
    plt.show()
    
def getAdvancedFeatures(df):
    df = df[df.columns[:47]]
    X = df.values
    
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(X)
    
     # Instantiate k-means and dbscan algorithms
    kmeans = KMeans(n_clusters=2)
    dbscan = DBSCAN(eps=0.3)
    
    # Fit the algorithms to the features
    kmeans.fit(scaled_features)
    dbscan.fit(scaled_features)
    
    # Compute the silhouette scores for each algorithm
    kmeans_silhouette = silhouette_score(
        scaled_features, kmeans.labels_
    ).round(2)
    dbscan_silhouette = silhouette_score(
       scaled_features, dbscan.labels_
    ).round (2)
    
    print("K-Means: ", kmeans_silhouette)
    print("DB Scan: ", dbscan_silhouette)
    
    # Plot the data and cluster silhouette comparison
    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(8, 6), sharex=True, sharey=True
    )
    fig.suptitle(f"Clustering Algorithm Comparison: Crescents", fontsize=16)
    fte_colors = {
        0: "#008fd5",
        1: "#fc4f30",
    }
    # The k-means plot
    km_colors = [fte_colors[label] for label in kmeans.labels_]
    ax1.scatter(scaled_features[:, 0], scaled_features[:, 1], c=km_colors)
    ax1.set_title(
        f"k-means\nSilhouette: {kmeans_silhouette}", fontdict={"fontsize": 12}
    )
    
    # The dbscan plot
    db_colors = [fte_colors[label] for label in dbscan.labels_]
    ax2.scatter(scaled_features[:, 0], scaled_features[:, 1], c=db_colors)
    ax2.set_title(
        f"DBSCAN\nSilhouette: {dbscan_silhouette}", fontdict={"fontsize": 12}
    )
    plt.show()
         
    