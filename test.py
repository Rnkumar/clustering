from sklearn.cluster import DBSCAN
import numpy as np

def recursive_dbscan(orders, min_radius, max_radius):
    clus = list()
    av_cluster_size = 3
    max_av_cluster_size = 2
    max_len_cluster = 10
    min_no_clusters = 2
    best_res=list()
    while min_radius < max_radius:
        curr_radius = (min_radius+max_radius)/2
        clusters = DBSCAN().fit(orders)
        db1_labels = clusters.labels_
        labels, no_of_clusters = np.unique(db1_labels[db1_labels>=0], return_counts=True)

        if no_of_clusters < min_no_clusters:
            max_radius = curr_radius - 1
        else:
            min_radius = curr_radius + 1
        
        if av_cluster_size > max_av_cluster_size:
            
            for k in range(no_of_clusters):
                clus.append(list())
            for i in range(len(db1_labels)):
                clus[i].append(orders[i])
            best_res = clus
            max_av_cluster_size = av_cluster_size
    for cluster in best_res:
        if len(cluster) > max_len_cluster:
            best_res.remove(cluster)
            best_res.append(recursive_dbscan(cluster,50,100))
    return clus

def dbScan(orders):
    clusters = DBSCAN().fit(orders)
    return clusters.labels_

o = list([[13.0481,77.6284],[13.1049,77.6723],[13.0897,77.6884],[13.1216,77.6754],[13.0922,77.6654],[13.0775,77.5758],[13.0684,77.5506]])
print(len(recursive_dbscan(o,50,100)))
print(dbScan(o))