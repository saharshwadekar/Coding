import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Scale the features for clustering
scaler = StandardScaler()
scaled_features = scaler.fit_transform(iris_df)

# Apply K-means clustering with k=3 (assuming 3 clusters)
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(scaled_features)

# Add cluster labels to the dataset
iris_df['Cluster'] = kmeans.labels_

# Visualize the clusters (2D plot for simplicity, using sepal length and width)
plt.figure(figsize=(8, 6))
plt.scatter(iris_df['sepal length (cm)'], iris_df['sepal width (cm)'], c=iris_df['Cluster'], cmap='viridis')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Customer Segmentation using K-means Clustering')
plt.colorbar(label='Cluster')
plt.show()
