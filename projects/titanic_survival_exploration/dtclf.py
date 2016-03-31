import numpy as np
import pandas as pd
import sys
from time import time
from sklearn import tree
from sklearn.metrics import accuracy_score

class ClfSurvivor:
    def __init__(self):
        self.loadData()
        return
    def loadData(self):
        in_file = 'titanic_data.csv'
        full_data = pd.read_csv(in_file)
        # Store the 'Survived' feature in a new variable and remove it from the dataset
        self.outcomes = full_data['Survived'].copy()
        self.data = full_data.drop(['Survived','Name','Ticket','Cabin','Embarked','PassengerId'], axis = 1).copy()
        self.data.fillna(-1, inplace=True)
        self.data.replace({'Sex' : { 'male' : 0, 'female' : 1}},  inplace=True) 
        return
    def prepareData(self):
        self.features_train = self.data
        self.labels_train = self.outcomes
        return
    def train(self):
        self.prepareData()
        clf = tree.DecisionTreeClassifier(min_samples_split = 2)
        clf = clf.fit(self.features_train, self.labels_train)
        y_pred=clf.predict(self.features_train)
        accuracy = accuracy_score(self.labels_train,y_pred )
        print "training set accuracy is %f" %(accuracy)
        return
    def run(self):
        self.train()
        return
    
    


if __name__ == "__main__":   
    obj= ClfSurvivor()
    obj.run()