# Import libraries
from PrepareData import PrepareData
import time
from sklearn.metrics import f1_score
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.metrics import make_scorer


class TrainModel(PrepareData):
    def __init__(self):
        PrepareData.__init__(self)
        self.clf = self.getClf()
        self.tunedParams = self.getTunedParamterOptions()
        return
    def getClf(self):
        pass
    def predict_labels(self, clf, features, target):
#         print "Predicting labels using {}...".format(clf.__class__.__name__)
        start = time.time()
        y_pred = clf.predict(features)
        end = time.time()
        print "Prediction time (secs): {:.3f}".format(end - start)
        return f1_score(target.values, y_pred, pos_label= 1)
    
    def train_classifier(self,clf, X_train, y_train):
        print "Training {}...".format(clf.__class__.__name__)
        start = time.time()
        clf.fit(X_train, y_train)
        end = time.time()
        print "Training time (secs): {:.3f}".format(end - start)
        return
    def train_predict(self, clf, X_train, y_train, X_test, y_test):
        print "------------------------------------------"
        print "Training set size: {}".format(len(X_train))
        self.train_classifier(clf, X_train, y_train)
        print "F1 score for training set: {}".format(self.predict_labels(clf, X_train, y_train))
        print "F1 score for test set: {}".format(self.predict_labels(clf, X_test, y_test))
        return
    def run_with_variant_train_num(self):
        for used_num in [100, 200, 300]:
            self.train_predict(self.clf, self.X_train.iloc[:used_num], self.y_train.iloc[:used_num], self.X_test, self.y_test)
        return
    def run_with_full_train_num(self):
        print("******************Default {}".format(self.clf.__class__.__name__))
        self.train_classifier(self.clf, self.X_train,self.y_train)
        print('Default paramters {}'.format(self.clf))
        print("******************Default {}".format(self.clf.__class__.__name__))
        train_f1_score = self.predict_labels(self.clf, self.X_train, self.y_train)
        print "Prediction result(train set)  {:.3f}".format(train_f1_score)
        # Predict on test data
        print "Prediction result(test set)  {:.3f}".format(self.predict_labels(self.clf, self.X_test, self.y_test))
        return
    def getTunedParamterOptions(self):
        pass
    def run_extra(self):
        pass
    def run_with_GridSearchCV(self):
        print("******************Grid search {}".format(self.clf.__class__.__name__))
        start = time.time()
        cv=StratifiedShuffleSplit(self.y_train, n_iter=20, random_state = 42)
#         clf = GridSearchCV(self.clf, self.tunedParams, cv=cv, scoring='f1')
        clf = GridSearchCV(self.clf, self.tunedParams, cv=cv, verbose= 0, n_jobs=4, scoring=make_scorer(f1_score, pos_label=1))
        clf.fit(self.X_train, self.y_train)
        print("best parameters {}".format( clf.best_params_))
        print("best score {:.3f}".format(clf.best_score_ ))
        end = time.time()
        print "Training time (secs): {:.3f}".format(end - start)
        print("******************Grid search {}".format(self.clf.__class__.__name__))
        res = self.predict_labels(clf.best_estimator_, self.X_train, self.y_train)
        print "Prediction result(train set)  {:.3f}".format(res)
        res = self.predict_labels(clf.best_estimator_, self.X_test, self.y_test)
        print "Prediction result(test set)  {:.3f}".format(res)
        return
    def run(self):
        self.preParedata()
        options ={1: self.run_with_GridSearchCV,
                  2: self.run_with_full_train_num,
                  3: self.run_with_variant_train_num}
        options[2]()
#         self.run_with_GridSearchCV()
#         self.run_with_full_train_num()
        
        
#         self.run_with_variant_train_num()
        self.run_extra()
        

        return
    




if __name__ == "__main__":   
    obj= TrainModel()
    obj.run()