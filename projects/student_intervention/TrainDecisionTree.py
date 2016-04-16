# Import libraries

from TrainModel import TrainModel
from sklearn import tree
import numpy as np

class TrainDecisionTree(TrainModel):
    def __init__(self):
        TrainModel.__init__(self)
        return
    def getClf(self):
        clf = tree.DecisionTreeClassifier(min_samples_split=5, random_state=100)
        return clf
    
    def getTunedParamterOptions(self):
        parameters = {'min_samples_split':np.arange(2,10), 'max_depth':np.arange(2,10)}
        return parameters



if __name__ == "__main__":   
    obj= TrainDecisionTree()
    obj.run()