# Import libraries

from TrainModel import TrainModel
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

class TrainKNNModel(TrainModel):
    def __init__(self):
        TrainModel.__init__(self)
        return
    def getTunedParamterOptions(self):
        parameters = {'n_neighbors':np.arange(4,31,2), 'p':[1, 2]}
        return parameters
    def getClf(self):
        clf = KNeighborsClassifier()
        return clf




if __name__ == "__main__":   
    obj= TrainKNNModel()
    obj.run()