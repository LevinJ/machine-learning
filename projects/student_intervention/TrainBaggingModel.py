# Import libraries

from TrainModel import TrainModel
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from PrepareData import ScaleMethod
from PrepareData import FeatureSelMethod
from sklearn.ensemble import RandomForestClassifier

class TrainBaggingModel(TrainModel):
    def __init__(self):
        TrainModel.__init__(self)
        self.scaling = ScaleMethod.MIN_MAX
        self.selectedFeatures = FeatureSelMethod.NONE
        return
    def getClf(self):
#         clf = BaggingClassifier(base_estimator=KNeighborsClassifier(), n_estimators=10, max_samples=0.5, max_features=0.5, random_state = 42)
#         clf = BaggingClassifier(base_estimator=DecisionTreeClassifier(), n_estimators=10, max_samples=0.5, max_features=0.5, random_state = 42)
        clf = RandomForestClassifier(n_estimators=10)
        return clf



if __name__ == "__main__":   
    obj= TrainBaggingModel()
    obj.run()