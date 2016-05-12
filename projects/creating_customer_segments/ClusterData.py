from projects.creating_customer_segments import renders_local as rs
import matplotlib.pyplot as plt
from projects.creating_customer_segments import TransformData
from sklearn.cluster import KMeans
from sklearn.mixture import GMM
from sklearn import metrics
from TransformData import TransformData
import pandas as pd
import numpy as np


class ClusterData(TransformData):
    def __init__(self):
        TransformData.__init__(self)
        return
    def run(self):
        self.transformData()
#         self.visualizeUnderlyingData()
        self.doClustering()
        self.barPlotDatapoints()
#         self.dataRecovery()
        plt.show()
        return
    def dataRecovery(self):
        # TODO: Inverse transform the centers
        log_centers = self.pca.inverse_transform(self.centers)
        
        # TODO: Exponentiate the centers
        true_centers = np.exp(log_centers)
        
        # Display the true centers
        segments = ['Segment {}'.format(i) for i in range(0,len(self.centers))]
        true_centers = pd.DataFrame(np.round(true_centers), columns = self.data.keys())
        true_centers.index = segments
        print(true_centers)
        return
    def GMMClusering(self):
        for n in range(2, 6):
            clusterer = GMM(n_components=n, random_state=42)
            clusterer.fit(self.reduced_data)
            preds = clusterer.predict(self.reduced_data)
    #         centers =  clusterer.cluster_centers_
            centers =  clusterer.means_ 
            sample_preds = clusterer.predict(self.pca_samples)
            score = metrics.silhouette_score(self.reduced_data, preds, metric='sqeuclidean')
            print("GMM with cluster number %d, score %0.3f"% (n, score))
        return
    def KMeansClusering(self):
        for n in range(2,6):
            clusterer = KMeans(n_clusters=n, random_state=42)
            clusterer.fit(self.reduced_data)
            preds = clusterer.predict(self.reduced_data)
            centers =  clusterer.cluster_centers_
            sample_preds = clusterer.predict(self.pca_samples)
            score = metrics.silhouette_score(self.reduced_data, preds, metric='sqeuclidean')
            print("K Means with cluster number %d, score %0.3f"% (n, score))
        return
    def optimalClustering(self):
        n =2
        clusterer = KMeans(n_clusters=n, random_state=42)
        clusterer.fit(self.reduced_data)
        preds = clusterer.predict(self.reduced_data)
        self.centers =  clusterer.cluster_centers_
        sample_preds = clusterer.predict(self.pca_samples)
        score = metrics.silhouette_score(self.reduced_data, preds, metric='sqeuclidean')
        print("K Means with cluster number %d, score %0.3f"% (n, score))
        rs.cluster_results(self.reduced_data, preds, self.centers, self.pca_samples)
        
        return
    def barPlotDatapoints(self):
        fig, ax = plt.subplots()
        n_groups = 5
        index = np.arange(n_groups)
        bar_width = 0.35
        
        opacity = 0.4
        error_config = {'ecolor': '0.3'}
        rects1 = plt.bar(index, self.centers[:,0].tolist() + self.pca_samples.iloc[:,0].tolist(), bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config,
                 label='Dim 1')
        
        rects2 = plt.bar(index + bar_width, self.centers[:,1].tolist() + self.pca_samples.iloc[:,1].tolist(), bar_width,
                 alpha=opacity,
                 color='r',
                 error_kw=error_config,
                 label='Dim 2')
        
        plt.xlabel('Data points')
        plt.ylabel('Scores')
        plt.title('Scores by datpoint and dimensions')
        plt.xticks(index + bar_width, ('Seg0', 'Seg1','S0','S1','S2'))
        plt.legend()
        return
    def visualizeUnderlyingData(self):
        rs.channel_results(self.reduced_data, self.outliers, self.pca_samples)
        return
    def doClustering(self):
#         self.GMMClusering()
#         self.KMeansClusering()
        self.optimalClustering()
#         clusterer = KMeans(n_clusters=4, random_state=42)

        
        return
    





if __name__ == "__main__":   
    obj= ClusterData()
    obj.run()