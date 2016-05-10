# Import libraries
import numpy as np
import pandas as pd
from ExploreData import ExploreData
from sklearn.cross_validation import train_test_split
from enum import Enum
from sklearn import preprocessing
import matplotlib.pyplot as plt
import os.path
from sklearn import preprocessing

class PrepareData(ExploreData):
    def __init__(self):
        ExploreData.__init__(self)
        return
    
    def performScaling(self):
        self.log_data = pd.DataFrame(np.log(self.data), columns=self.data.columns)
        self.log_samples = pd.DataFrame(np.log(self.samples), columns=self.samples.columns)
        fname = "customers_log.csv"
        if not os.path.isfile(fname):
            self.log_data.to_csv(fname)
            scaler = preprocessing.StandardScaler()
            self.data_log_std = pd.DataFrame(scaler.fit_transform(self.log_data), columns=self.log_data.columns)
            self.data_log_std.to_csv("customers_log_std.csv")
        
        pd.scatter_matrix(self.log_data, alpha = 0.3, figsize = (14,8), diagonal = 'kde')
        print(self.log_samples)
#         plt.show()
        return
    def RemoveOutlier(self):
        # For each feature find the data points with extreme high or low values
        outliers = pd.DataFrame(columns = list(self.log_data.columns) + ['ol_count'])
        for feature in self.log_data.keys():
            
            # TODO: Calculate Q1 (25th percentile of the data) for the given feature
            Q1 = np.percentile(self.log_data[feature], 25)
            
            # TODO: Calculate Q3 (75th percentile of the data) for the given feature
            Q3 =np.percentile(self.log_data[feature], 75)
            
            # TODO: Use the interquartile range to calculate an outlier step (1.5 times the interquartile range)
            step = 1.5 * (Q3 - Q1)
            
            # Display the outliers
            print "####outliers '{}: {}---{}':".format(feature,Q1 - step, Q3 + step)
            print(self.log_data[~((self.log_data[feature] >= Q1 - step) & (self.log_data[feature] <= Q3 + step))])
            outlier = self.log_data[~((self.log_data[feature] >= Q1 - step) & (self.log_data[feature] <= Q3 + step))]
            for rowid, row in outlier.iterrows():
                if rowid in outliers.index:
                    curvalue = outliers.loc[rowid, 'ol_count']
                    outliers.loc[rowid, 'ol_count'] = curvalue + 1
                else:
                    row = pd.DataFrame(np.array(list(row) + [1]).reshape((1,-1)), index =[rowid], columns = list(outliers.columns))
                    outliers = pd.concat([outliers, row])
            
        
        #print out data points considered as outliers for more than one feature 
        print("****potential outliers***")
        print(outliers.loc[outliers['ol_count'] >= 2])   
#         outliers  = [154,75,65,66,128]    
#         outliers  = [75,66,128,154] 
        self.outliers  = [128,66,65,75,154] 
#         self.outliers  = [] 
        # OPTIONAL: Select the indices for data points you wish to remove
#         outliers  = [66,128,75]
        
        # Remove the outliers, if any were specified
        self.good_data = self.log_data.drop(self.log_data.index[self.outliers]).reset_index(drop = True)
        return
    def prepareData(self):
        self.performScaling()
        self.RemoveOutlier()
        return
    def run(self): 
        self.prepareData()   
        self.featureRelevance(self.log_data)
        return
    




if __name__ == "__main__":   
    obj= PrepareData()
    obj.run()
    
    
    