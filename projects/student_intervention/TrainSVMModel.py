# Import libraries

from TrainModel import TrainModel
from sklearn.svm import SVC
import numpy as np

class TrainSVMModel(TrainModel):
    def __init__(self):
        TrainModel.__init__(self)
        return
    def getClf(self):
        clf = SVC(C=0.5, kernel='rbf', gamma=0.2)
        return clf
    def getTunedParamterOptions(self):
        parameters = {'C':np.logspace(-2, 10, 5), 'gamma':np.logspace(-9, 3, 5)}
        return parameters




if __name__ == "__main__":   
    obj= TrainSVMModel()
    obj.run()