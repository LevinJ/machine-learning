# Importing a few necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor


class DataExploration:
    def __init__(self):
        # Create our client's feature set for which we will be predicting a selling price
        self.CLIENT_FEATURES = [[11.95, 0.00, 18.100, 0, 0.6590, 5.6090, 90.00, 1.385, 24, 680.0, 20.20, 332.09, 12.13]]
        # Load the Boston Housing dataset into the city_data variable
        self.city_data = datasets.load_boston()
        # Initialize the housing prices and housing features
        self.housing_prices = self.city_data.target
        self.housing_features = self.city_data.data
        print "Boston Housing dataset loaded successfully!"
        return
    def showStats(self):
        housing_prices = self.housing_prices
        housing_features = self.housing_features
        # Number of houses in the dataset
        total_houses = housing_prices.shape[0]
        
        # Number of features in the dataset
        total_features = housing_features.shape[1]
        
        # Minimum housing value in the dataset
        minimum_price = housing_prices.min()
        
        # Maximum housing value in the dataset
        maximum_price = housing_prices.max()
        
        # Mean house value of the dataset
        mean_price = housing_prices.mean()
        
        # Median house value of the dataset
        median_price = np.median(housing_prices)
        
        # Standard deviation of housing values of the dataset
        std_dev = np.std(housing_prices)
        
        # Show the calculated statistics
        print "Boston Housing dataset statistics (in $1000's):\n"
        print "Total number of houses:", total_houses
        print "Total number of features:", total_features
        print "Minimum house price:", minimum_price
        print "Maximum house price:", maximum_price
        print "Mean house price: {0:.3f}".format(mean_price)
        print "Median house price:", median_price
        print "Standard deviation of house price: {0:.3f}".format(std_dev)
        return
    def savetoCSV(self):
        df = pd.DataFrame(data = np.column_stack((self.city_data.data, self.city_data.target)), 
                          columns = np.concatenate((self.city_data.feature_names, np.array(['Prices'])),axis=0))
        df.to_csv("bostonhousing.csv")
        return
    def run(self):
        self.showStats()
#         self.savetoCSV()
        return
    




if __name__ == "__main__":   
    obj= DataExploration()
    obj.run()