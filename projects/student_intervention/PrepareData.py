# Import libraries
import numpy as np
import pandas as pd
from ExploreData import ExploreData
from sklearn.cross_validation import train_test_split
from enum import Enum
from sklearn import preprocessing

class ScaleMethod(Enum):
    NONE = 1
    MIN_MAX = 2
    STD = 3

class FeatureSelMethod(Enum):
    NONE = 1
    VER1 = 2
    VER2 = 3

class PrepareData(ExploreData):
    def __init__(self):
        ExploreData.__init__(self)
        self.num_train = 300  # about 75% of the data
        self.scaling = ScaleMethod.NONE
        self.selectedFeatures = FeatureSelMethod.NONE
        return
    def getAllFeatureTarget(self):
        student_data = self.student_data
        # Extract feature (X) and target (y) columns
        feature_cols = list(student_data.columns[:-1])  # all columns but last are features
        target_col = student_data.columns[-1]  # last column is the target/label
        print "Feature column(s):-\n{}".format(feature_cols)
        print "Target column: {}".format(target_col)
        
        self.X_all = student_data[feature_cols]  # feature values for all students
        self.y_all = student_data[target_col]  # corresponding targets/labels
#         print "\nFeature values:-"
#         print self.X_all.head()  # print the first 5 rows
        return
    def savePreprocessedfeatures(self, X_all, y_all):
        df = pd.concat([X_all, y_all], axis=1)
        print df.describe()
        df.to_csv("featureslabels.csv")
        return
    # Preprocess feature columns
    def transformCategories(self):
        outX = pd.DataFrame(index=self.X_all.index)  # output dataframe, initially empty
        # Check each column
        for col, col_data in self.X_all.iteritems():
            # If data type is non-numeric, try to replace all yes/no values with 1/0
            if col_data.dtype == object:
                col_data = col_data.replace(['yes', 'no'], [1, 0])
            # Note: This should change the data type for yes/no columns to int
    
            # If still non-numeric, convert to one or more dummy variables
            if col_data.dtype == object :
                col_data = pd.get_dummies(col_data, prefix=col)  # e.g. 'school' => 'school_GP', 'school_MS'
    
            outX = outX.join(col_data)  # collect column(s) in output dataframe
        return outX
    def preprocess_features(self):
        self.X_all = self.transformCategories()
        self.X_all = self.rescale(self.X_all) 
        self.X_all = self.selectFeatures(self.X_all)  
        return
    def selectFeatures(self, outX):
        if self.selectedFeatures is FeatureSelMethod.VER1 :
            outX = outX[['absences','failures','famrel','Medu']]
        return outX
    def splitDataTrainTest(self):
        # First, decide how many training vs test samples you want
        num_all = self.student_data.shape[0]  # same as len(student_data)
        num_test = num_all - self.num_train
        
        # TODO: Then, select features (X) and corresponding labels (y) for the training and test sets
        # Note: Shuffle the data or randomly select samples to avoid any bias due to ordering in the dataset
        self.y_all = self.y_all.replace(['yes', 'no'], [1, 0])
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X_all, self.y_all, test_size=num_test, random_state=42)
        
        print "Training set: {} samples".format(self.X_train.shape[0])
        print "Test set: {} samples".format(self.X_test.shape[0])
        # Note: If you need a validation set, extract it from within training data
        return
    def rescale(self, outX):
        scaler = None
        if self.scaling is ScaleMethod.STD:
            scaler = preprocessing.StandardScaler()
        elif self.scaling is ScaleMethod.MIN_MAX:
            scaler = preprocessing.MinMaxScaler()
        else:
            return outX
        outX[['age', 'absences']] = scaler.fit_transform(outX[['age', 'absences']])
        return outX
    def preParedata(self):
        self.getAllFeatureTarget()
        self.preprocess_features()
        self.splitDataTrainTest()
        return
    def run(self):
        self.preParedata()
        self.savePreprocessedfeatures(self.X_all, self.y_all)

        return
    




if __name__ == "__main__":   
    obj= PrepareData()
    obj.run()