# Importing a few necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor
from  EvaluateModel import EvaluateModel
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import make_scorer
import matplotlib
matplotlib.style.use('ggplot')


class AnalyzeModel(EvaluateModel):
    def __init__(self):
        EvaluateModel.__init__(self)
        return
    
    def run(self):
        EvaluateModel.run(self)
#         self.testLearningCurve()
        self.testmodel_complexity()
        return
    def testLearningCurve(self):
        X_train, y_train, X_test, y_test = self.shuffle_split_data(self.housing_features, self.housing_prices)
        self.learning_curves(X_train, y_train, X_test, y_test)
        return
    def testmodel_complexity(self):
        X_train, y_train, X_test, y_test = self.shuffle_split_data(self.housing_features, self.housing_prices)
        self.model_complexity(X_train, y_train, X_test, y_test)
        return
    def model_complexity(self,X_train, y_train, X_test, y_test):
        """ Calculates the performance of the model as model complexity increases.
            The learning and testing errors rates are then plotted. """
        
        print "Creating a model complexity graph. . . "
    
        # We will vary the max_depth of a decision tree model from 1 to 14
        max_depth = np.arange(1, 14)
        train_err = np.zeros(len(max_depth))
        test_err = np.zeros(len(max_depth))
    
        for i, d in enumerate(max_depth):
            # Setup a Decision Tree Regressor so that it learns a tree with depth d
            regressor = DecisionTreeRegressor(max_depth = d)
    
            # Fit the learner to the training data
            regressor.fit(X_train, y_train)
    
            # Find the performance on the training set
            train_err[i] = self.performance_metric(y_train, regressor.predict(X_train))
    
            # Find the performance on the testing set
            test_err[i] = self.performance_metric(y_test, regressor.predict(X_test))
    
        # Plot the model complexity graph
        pl.figure(figsize=(7, 5))
        pl.title('Decision Tree Regressor Complexity Performance')
        pl.plot(max_depth, test_err, lw=2, label = 'Testing Error')
        pl.plot(max_depth, train_err, lw=2, label = 'Training Error')
        pl.legend()
        pl.xlabel('Maximum Depth')
        pl.ylabel('Total Error')
        pl.show()
    def learning_curves(self,X_train, y_train, X_test, y_test):
        """ Calculates the performance of several models with varying sizes of training data.
            The learning and testing error rates for each model are then plotted. """
        
        print "Creating learning curve graphs for max_depths of 1, 3, 6, and 10. . ."
        
        # Create the figure window
        fig = pl.figure(figsize=(10,8))
    
        # We will vary the training set size so that we have 50 different sizes
        sizes = np.rint(np.linspace(1, len(X_train), 50)).astype(int)
        train_err = np.zeros(len(sizes))
        test_err = np.zeros(len(sizes))
    
        # Create four different models based on max_depth
        for k, depth in enumerate([1,3,6,10]):
            
            for i, s in enumerate(sizes):
                
                # Setup a decision tree regressor so that it learns a tree with max_depth = depth
                regressor = DecisionTreeRegressor(max_depth = depth)
                
                # Fit the learner to the training data
                regressor.fit(X_train[:s], y_train[:s])
    
                # Find the performance on the training set
                train_err[i] = self.performance_metric(y_train[:s], regressor.predict(X_train[:s]))
                
                # Find the performance on the testing set
                test_err[i] = self.performance_metric(y_test, regressor.predict(X_test))
    
            # Subplot the learning curve graph
            ax = fig.add_subplot(2, 2, k+1)
            ax.plot(sizes, test_err, lw = 2, label = 'Testing Error')
            ax.plot(sizes, train_err, lw = 2, label = 'Training Error')
            ax.legend()
            ax.set_title('max_depth = %s'%(depth))
            ax.set_xlabel('Number of Data Points in Training Set')
            ax.set_ylabel('Total Error')
            ax.set_xlim([0, len(X_train)])
        
        # Visual aesthetics
        fig.suptitle('Decision Tree Regressor Learning Performances', fontsize=18, y=1.03)
        fig.tight_layout()
        fig.show()
        pl.show()
   



if __name__ == "__main__":   
    obj= AnalyzeModel()
    obj.run()