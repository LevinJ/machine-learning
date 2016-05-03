# Import libraries
from PrepareData import PrepareData
from sklearn.decomposition import PCA
import renders as rs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os.path

class TransformFeature(PrepareData):
    def __init__(self):
        PrepareData.__init__(self)
        return
    
    def run(self):
        self.prepareData()
        self.pca_transform()
        return
    def savetransformeddata(self, pca):
        pca_data = pca.transform(self.good_data)
        columns = []
        for i in range(6):
            columns.append("Dimension" + str(i+1))
        pca_data = pd.DataFrame(np.round(pca_data, 4), columns = columns)
        fname = "customers_pca.csv"
        if not os.path.isfile(fname):
            pca_data.to_csv(fname)
        return
    def pca_transform(self):
        # TODO: Apply PCA to the good data with the same number of dimensions as features
        pca = PCA().fit(self.good_data)
        # Generate PCA results plot
        pca_results = rs.pca_results(self.good_data, pca)
        self.savetransformeddata(pca)
        print "################trnsformed sample data#########"
        # TODO: Apply a PCA transformation to the sample log-data
        pca_samples = pca.transform(self.log_samples)
        print pd.DataFrame(np.round(pca_samples, 4), columns = pca_results.index.values)
        
        plt.show()
        return



if __name__ == "__main__":   
    obj= TransformFeature()
    obj.run()