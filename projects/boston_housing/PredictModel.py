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
from  DataExploration import DataExploration

class PredictModel(EvaluateModel):
    def __init__(self):
        EvaluateModel.__init__(self)
        return
    
    def run(self):
        DataExploration.run(self)
        reg = self.testFitmodel()
        sale_price = reg.predict(self.CLIENT_FEATURES)
        print "Predicted value of client's home: {0:.3f}".format(sale_price[0])
        return



if __name__ == "__main__":   
    obj= PredictModel()
    obj.run()