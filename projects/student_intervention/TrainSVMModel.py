# Import libraries

from TrainModel import TrainModel
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from PrepareData import ScaleMethod
        
class TrainSVMModel(TrainModel):
    def __init__(self):
        TrainModel.__init__(self)
        self.scaling = ScaleMethod.NONE
        return
    def getClf(self):
        clf = SVC(C=1, gamma=0.07)
        return clf
    def getTunedParamterOptions(self):
#         parameters = {'C':np.logspace(-2, 10, num=5,base=2.0), 'gamma':np.logspace(-9, 3, num=5,base=2.0)}
#         parameters = {'C':[1,10,100], 'gamma':[0.01, 0.07, 1,10]}
#         parameters = {'C':[1], 'gamma':[0.07, 1,10]}
        parameters = {'C':np.logspace(-2, 5, num=8,base=10.0), 'gamma':np.logspace(-2, 5, num=8,base=10.0)}
        return parameters




if __name__ == "__main__":   
    obj= TrainSVMModel()
    obj.run()