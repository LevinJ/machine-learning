# Import libraries

from TrainModel import TrainModel
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from PrepareData import ScaleMethod
from PrepareData import FeatureSelMethod
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC


class TrainBoostingModel(TrainModel):
    def __init__(self):
        TrainModel.__init__(self)
        self.scaling = ScaleMethod.STD
        self.selectedFeatures = FeatureSelMethod.VER1
        return
    def getClf(self):
#         clf = AdaBoostClassifier(base_estimator = DecisionTreeClassifier(max_depth=1))
        clf = AdaBoostClassifier(base_estimator = SVC(probability = True),n_estimators=500)
#         clf = AdaBoostClassifier(clf = SVC(probability=True,kernel='linear'), n_estimators=500,random_state = 42)
#         clf = AdaBoostClassifier(n_estimators=500,random_state = 42)
        return clf



if __name__ == "__main__":   
    obj= TrainBoostingModel()
    obj.run()