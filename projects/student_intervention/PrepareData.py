# Import libraries
import numpy as np
import pandas as pd
from ExploreData import ExploreData
from sklearn.cross_validation import train_test_split


class PrepareData(ExploreData):
    def __init__(self):
        ExploreData.__init__(self)
        self.num_train = 300  # about 75% of the data
        self.getAllFeatureTarget()
        self.splitDataTrainTest()
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
    # Preprocess feature columns
    def preprocess_features(self, X):
        outX = pd.DataFrame(index=X.index)  # output dataframe, initially empty
        # Check each column
        for col, col_data in X.iteritems():
            # If data type is non-numeric, try to replace all yes/no values with 1/0
            if col_data.dtype == object:
                col_data = col_data.replace(['yes', 'no'], [1, 0])
            # Note: This should change the data type for yes/no columns to int
    
            # If still non-numeric, convert to one or more dummy variables
            if col_data.dtype == object:
                col_data = pd.get_dummies(col_data, prefix=col)  # e.g. 'school' => 'school_GP', 'school_MS'
    
            outX = outX.join(col_data)  # collect column(s) in output dataframe

        return outX
    def splitDataTrainTest(self):
        # First, decide how many training vs test samples you want
        num_all = self.student_data.shape[0]  # same as len(student_data)
        num_test = num_all - self.num_train
        
        # TODO: Then, select features (X) and corresponding labels (y) for the training and test sets
        # Note: Shuffle the data or randomly select samples to avoid any bias due to ordering in the dataset
        X_all = self.preprocess_features(self.X_all)
        y_all = self.y_all.replace(['yes', 'no'], [1, 0])
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X_all, y_all, test_size=num_test, random_state=42)
        
        print "Training set: {} samples".format(self.X_train.shape[0])
        print "Test set: {} samples".format(self.X_test.shape[0])
        # Note: If you need a validation set, extract it from within training data
        return
    def run(self):
#         self.splitDataTrainTest()

        return
    




if __name__ == "__main__":   
    obj= PrepareData()
    obj.run()