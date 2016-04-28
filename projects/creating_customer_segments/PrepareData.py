# Import libraries
import numpy as np
import pandas as pd
from ExploreData import ExploreData
from sklearn.cross_validation import train_test_split
from enum import Enum
from sklearn import preprocessing
import matplotlib.pyplot as plt

class PrepareData(ExploreData):
    def __init__(self):
        ExploreData.__init__(self)
        return
    
    def performScaling(self):
        self.log_data = pd.DataFrame(np.log(self.data), columns=self.data.columns)
        self.log_samples = pd.DataFrame(np.log(self.samples), columns=self.samples.columns)
        pd.scatter_matrix(self.log_data, alpha = 0.3, figsize = (14,8), diagonal = 'kde')
        print(self.log_samples)
#         plt.show()
        return
    def run(self):
        self.performScaling()
        self.featureRelevance(self.log_data)
        return
    




if __name__ == "__main__":   
    obj= PrepareData()
    obj.run()