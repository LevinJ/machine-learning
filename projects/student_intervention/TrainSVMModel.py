# Import libraries

from TrainModel import TrainModel
from sklearn.svm import SVC
import numpy as np

class TrainSVMModel(TrainModel):
    def __init__(self):
        TrainModel.__init__(self)
        return
    def getClf(self):
        clf = SVC(C=1, gamma=0.07)
        return clf
    def getTunedParamterOptions(self):
#         parameters = {'C':np.logspace(-2, 10, num=5,base=2.0), 'gamma':np.logspace(-9, 3, num=5,base=2.0)}
#         parameters = {'C':[1,10,100], 'gamma':[0.01, 0.07, 1,10]}
        parameters = {'C':[1], 'gamma':[0.07, 1,10]}
        return parameters




if __name__ == "__main__":   
    obj= TrainSVMModel()
    obj.run()