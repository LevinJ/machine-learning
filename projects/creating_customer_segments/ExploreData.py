# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeRegressor


class ExploreData:
    def __init__(self):
        # Read student data
        self.data = pd.read_csv("customers.csv")
        self.data.drop(['Region', 'Channel'], axis = 1, inplace = True)
        self.selectsamples()
        
        return
    def selectsamples(self):
        indices = [71,196,333]
#         Create a DataFrame of the chosen samples
        self.samples = pd.DataFrame(self.data.loc[indices], columns = self.data.keys()).reset_index(drop = True)
        print(self.samples)
        return
    def showStats(self):
        print("Wholesale customers dataset has {} samples with {} features each.".format(*self.data.shape))
        self.selectsamples()
        print(self.data.describe())
        return
    def visualize_scatter(self):
        pd.scatter_matrix(self.data, alpha = 0.3, figsize = (14,8), diagonal = 'kde');
        plt.show()
        return
    def visualize_hist(self):
#         self.data[['Detergents_Paper']].hist(color='k', alpha=0.5, bins=10)
        self.data.hist(color='k', alpha=0.5, bins=50)
#         pd.scatter_matrix(self.data, alpha = 0.3, figsize = (14,8), diagonal = 'kde');
        plt.show()
        return
    def rescale(self):
        scaler = preprocessing.StandardScaler()
        self.data_scaled = pd.DataFrame(scaler.fit_transform(self.data), columns=self.data.columns)
        self.data_scaled[60:70].plot.bar()
#         self.data_scaled.to_csv("customers_scaled.csv")
        plt.show()
        
        return
    def featureRelevance(self, data):
        testFeature = 'Detergents_Paper'
        new_data = data.drop([testFeature], axis = 1)
        X_train, X_test, y_train, y_test = train_test_split(new_data, data[[testFeature]], test_size=0.25, random_state=42)
        regressor = DecisionTreeRegressor(random_state=30).fit(X_train, y_train)
        score = regressor.score(X_test, y_test)
        print("feature relevance test: feature {}, score {}".format(testFeature, score))
        return
    def run(self):
        self.showStats()
        self.featureRelevance(self.data)
#         self.rescale()
#         self.visualize_hist()
            
        return
    




if __name__ == "__main__":   
    obj= ExploreData()
    obj.run()