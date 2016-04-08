# Importing a few necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor
from  DataExploration import DataExploration
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.cross_validation import ShuffleSplit


class EvaluateModel(DataExploration):
    def __init__(self):
        DataExploration.__init__(self)
        return
    
    def run(self):
        DataExploration.run(self)
        self.testFitmodel()
#         self.testPerformanceMetrics()
#         self.testShuffleSplitData()
        return
    def testShuffleSplitData(self):
        # Test shuffle_split_data
        try:
            X_train, y_train, X_test, y_test = self.shuffle_split_data(self.housing_features, self.housing_prices)
            print "Successfully shuffled and split the data!"
        except:
            print "Something went wrong with shuffling and splitting the data."
        return X_train, y_train, X_test, y_test 
    def testPerformanceMetrics(self):
        # Test performance_metric
        try:
            X_train, y_train, X_test, y_test  = self.testShuffleSplitData()
            total_error = self.performance_metric(y_train, y_train)
            print "Successfully performed a metric calculation!", total_error
        except:
            print "Something went wrong with performing a metric calculation."
        return total_error
    def performance_metric(self, y_true, y_predict):
        """ Calculates and returns the total error between true and predicted values
        based on a performance metric chosen by the student. """

        error = mean_squared_error(y_true, y_predict)
        return error
    def dispFeatureImportance(self, reg):
        features_list = self.city_data.feature_names
        sortIndexes = reg.feature_importances_.argsort()[::-1]
        features_rank = features_list[sortIndexes]
        num_rank = reg.feature_importances_[sortIndexes]
        print "Ranked features: {}".format(features_rank)
        print "Ranked importance: {}".format(num_rank)
        return
    def fit_model(self, X, y):
        """ Tunes a decision tree regressor model using GridSearchCV on the input data X 
            and target labels y and returns this optimal model. """
        performance_metric = self.performance_metric
    
        # Create a decision tree regressor object
        regressor = DecisionTreeRegressor()
    
        # Set up the parameters we wish to tune
        parameters = {'max_depth':(1,2,3,4,5,6,7,8,9,10)}
    
        # Make an appropriate scoring function
        scoring_function = make_scorer(performance_metric, greater_is_better = False)
        
        cv = ShuffleSplit(y.shape[0], n_iter=1000,  test_size=0.3, random_state=42)
    
        # Make the GridSearchCV object
        reg = GridSearchCV(regressor, parameters, scoring  = scoring_function, cv = cv)
    
        # Fit the learner to the data to obtain the optimal model with tuned parameters
        reg.fit(X, y)
        print "best score {}".format(reg.best_score_)
        print "best parameters {}".format(reg.best_params_)
        self.dispFeatureImportance(reg.best_estimator_)
    
        # Return the optimal model
        return reg.best_estimator_
    def testFitmodel(self):
        # Test fit_model on entire dataset
        try:
            reg = self.fit_model(self.housing_features, self.housing_prices)
            print "Final model has an optimal max_depth parameter of", reg.get_params()['max_depth']
        except:
            print "Something went wrong with fitting a model."
        return reg
    def shuffle_split_data(self,X, y):
        """ Shuffles and splits data into 70% training and 30% testing subsets,
            then returns the training and testing subsets. """
    
        # Shuffle and split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
        # Return the training and testing data subsets
        return X_train, y_train, X_test, y_test



if __name__ == "__main__":   
    obj= EvaluateModel()
    obj.run()