import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
#df = pd.read_csv('summer-travel-gps-full.csv')
coords = np.array([[13.0544,77.6047],[13.0499,77.6122],[13.0228,77.7714],[13.0915,77.6414]])
kms_per_radian = 6371.0088
epsilon = 7 / kms_per_radian
db = DBSCAN(eps=epsilon, min_samples=1, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
cluster_labels = db.labels_
print(cluster_labels)
num_clusters = len(set(cluster_labels))
clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])
print(clusters)
print('Number of clusters: {}'.format(num_clusters))