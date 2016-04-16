# Import libraries

from TrainModel import TrainModel
from sklearn.tree import DecisionTreeClassifier
import numpy as np

class TrainDecisionTree(TrainModel):
    def __init__(self):
        TrainModel.__init__(self)
        return
    def getClf(self):
        clf = DecisionTreeClassifier(random_state=100)
        return clf
    
    def getTunedParamterOptions(self):
        parameters = {'min_samples_split':np.arange(2,10), 'max_depth':np.arange(2,10)}
        return parameters
    def dispFeatureImportance(self, clf):
        if not hasattr(clf, 'feature_importances_'):
            return
        features_list = self.X_all.columns
        sortIndexes = clf.feature_importances_.argsort()[::-1]
        features_rank = features_list[sortIndexes]
        num_rank = clf.feature_importances_[sortIndexes]
        print "Ranked features: {}".format(features_rank)
        print "Ranked importance: {}".format(num_rank)
        return
    def run_extra(self):
        self.dispFeatureImportance(self.clf)



if __name__ == "__main__":   
    obj= TrainDecisionTree()
    obj.run()