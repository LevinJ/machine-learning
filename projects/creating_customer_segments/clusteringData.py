from PrepareData import PrepareData
from sklearn.decomposition import PCA
import renders as rs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os.path
from TransformFeature import TransformFeature
from sklearn.cluster import KMeans
from sklearn.mixture import GMM
from sklearn import metrics


class ClusteringData(TransformFeature):
    def __init__(self):
        TransformFeature.__init__(self)
        return
    def run(self):
        self.transformFeature()
        self.doClustering()
        plt.show()
        return
    def GMMClusering(self):
        for n in range(2, 6):
            clusterer = GMM(n_components=n, random_state=42)
            clusterer.fit(self.reduced_data)
            preds = clusterer.predict(self.reduced_data)
    #         centers =  clusterer.cluster_centers_
            centers =  clusterer.means_ 
            sample_preds = clusterer.predict(self.reduced_samples)
            score = metrics.silhouette_score(self.reduced_data, preds, metric='sqeuclidean')
            print("GMM component %d, score %0.3f"% (n, score))
        return
    def KNNClusering(self):
        for n in range(2,6):
            clusterer = KMeans(n_clusters=n, random_state=42)
            clusterer.fit(self.reduced_data)
            preds = clusterer.predict(self.reduced_data)
            centers =  clusterer.cluster_centers_
            sample_preds = clusterer.predict(self.reduced_samples)
            score = metrics.silhouette_score(self.reduced_data, preds, metric='sqeuclidean')
            print("KNN component %d, score %0.3f"% (n, score))
        return
    def optimalClustering(self):
        n =2
        clusterer = KMeans(n_clusters=n, random_state=42)
        clusterer.fit(self.reduced_data)
        preds = clusterer.predict(self.reduced_data)
        centers =  clusterer.cluster_centers_
        sample_preds = clusterer.predict(self.reduced_samples)
        score = metrics.silhouette_score(self.reduced_data, preds, metric='sqeuclidean')
        print("KNN component %d, score %0.3f"% (n, score))
        rs.cluster_results(self.reduced_data, preds, centers, self.reduced_samples)
        
        return
    def doClustering(self):
#         self.GMMClusering()
#         self.KNNClusering()
        self.optimalClustering()
#         clusterer = KMeans(n_clusters=4, random_state=42)

        
        return
    





if __name__ == "__main__":   
    obj= ClusteringData()
    obj.run()